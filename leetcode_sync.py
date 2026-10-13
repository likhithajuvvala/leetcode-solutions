#!/usr/bin/env python3
"""Sync accepted LeetCode submissions into this repo, with a README per problem.

With --push, every submission becomes its own git commit dated when you actually
solved it, so your GitHub contribution graph reflects your real history.

Env vars required:
  LEETCODE_SESSION  - value of the LEETCODE_SESSION cookie
  LEETCODE_CSRF     - value of the csrftoken cookie

Usage:
  python leetcode_sync.py            # write files only
  python leetcode_sync.py --push     # also commit (one per submission) and push
"""
import argparse
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://leetcode.com"
SOLUTIONS_DIR = Path("solutions")
STATE_FILE = Path(".leetcode_sync_state.json")
DELAY = 1.5  # seconds between requests, be polite

EXT = {
    "python": "py", "python3": "py", "cpp": "cpp", "java": "java",
    "c": "c", "csharp": "cs", "javascript": "js", "typescript": "ts",
    "golang": "go", "rust": "rs", "ruby": "rb", "swift": "swift",
    "kotlin": "kt", "scala": "scala", "php": "php", "mysql": "sql",
    "mssql": "sql", "oraclesql": "sql", "postgresql": "sql", "bash": "sh",
    "dart": "dart", "racket": "rkt", "erlang": "erl", "elixir": "ex",
}

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    difficulty
    content
    topicTags { name }
  }
}
"""


def make_session():
    session_cookie = os.environ.get("LEETCODE_SESSION")
    csrf = os.environ.get("LEETCODE_CSRF")
    if not session_cookie or not csrf:
        sys.exit("Set LEETCODE_SESSION and LEETCODE_CSRF environment variables.")
    s = requests.Session()
    s.cookies.set("LEETCODE_SESSION", session_cookie, domain="leetcode.com")
    s.cookies.set("csrftoken", csrf, domain="leetcode.com")
    s.headers.update({
        "User-Agent": "Mozilla/5.0 (leetcode-github-sync)",
        "Referer": BASE,
        "x-csrftoken": csrf,
        "Content-Type": "application/json",
    })
    return s


def fetch_accepted(s, known_ids):
    """Yield accepted submissions, newest first. Stops once it hits a known one."""
    offset, limit = 0, 20
    while True:
        r = s.get(f"{BASE}/api/submissions/", params={"offset": offset, "limit": limit}, timeout=30)
        if r.status_code in (401, 403):
            sys.exit("LeetCode rejected the cookies. Refresh LEETCODE_SESSION / csrftoken.")
        r.raise_for_status()
        data = r.json()
        for sub in data.get("submissions_dump", []):
            if sub["id"] in known_ids:
                return
            if sub.get("status_display") == "Accepted":
                yield sub
        if not data.get("has_next"):
            return
        offset += limit
        time.sleep(DELAY)


def fetch_question(s, slug):
    r = s.post(f"{BASE}/graphql", data=json.dumps(
        {"query": QUESTION_QUERY, "variables": {"titleSlug": slug}}), timeout=30)
    r.raise_for_status()
    q = (r.json().get("data") or {}).get("question")
    if not q:
        raise RuntimeError(f"No question data for {slug}")
    return q


def problem_readme(q, sub, lang_ext):
    tags = ", ".join(t["name"] for t in q.get("topicTags", [])) or "-"
    link = f"{BASE}/problems/{sub['title_slug']}/"
    solved = datetime.fromtimestamp(int(sub["timestamp"]), tz=timezone.utc).strftime("%Y-%m-%d")
    content = q.get("content") or "<p>(Premium problem: description unavailable.)</p>"
    return f"""# {q['questionFrontendId']}. {q['title']}

**Difficulty:** {q['difficulty']}  
**Tags:** {tags}  
**Link:** [{link}]({link})

## My submission

| Language | Runtime | Memory | Solved on |
|---|---|---|---|
| {sub['lang']} | {sub.get('runtime', '-')} | {sub.get('memory', '-')} | {solved} |

Solution file: [`solution.{lang_ext}`](solution.{lang_ext})

## Problem

{content}
"""


def save_problem(q, sub):
    lang = sub["lang"]
    ext = EXT.get(lang, "txt")
    folder = SOLUTIONS_DIR / f"{int(q['questionFrontendId']):04d}-{sub['title_slug']}"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"solution.{ext}").write_text(sub["code"], encoding="utf-8")
    (folder / "README.md").write_text(problem_readme(q, sub, ext), encoding="utf-8")
    return {
        "id": int(q["questionFrontendId"]),
        "title": q["title"],
        "slug": sub["title_slug"],
        "difficulty": q["difficulty"],
        "lang": lang,
        "folder": folder.as_posix(),
    }


def write_root_readme(problems):
    rows = sorted(problems.values(), key=lambda p: p["id"])
    counts = {d: sum(1 for p in rows if p["difficulty"] == d) for d in ("Easy", "Medium", "Hard")}
    lines = [
        "# LeetCode Solutions",
        "",
        f"**Solved:** {len(rows)} (Easy {counts['Easy']} / Medium {counts['Medium']} / Hard {counts['Hard']})",
        "",
        "| # | Title | Difficulty | Language |",
        "|---|---|---|---|",
    ]
    for p in rows:
        lines.append(f"| {p['id']} | [{p['title']}]({p['folder']}/) | {p['difficulty']} | {p['lang']} |")
    Path("README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def git_commit(message, paths, ts):
    """Stage `paths` and commit them dated at unix time `ts`. Skips if nothing changed."""
    subprocess.run(["git", "add", "--", *paths], check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode == 0:
        return False
    when = f"{int(ts)} +0000"
    env = {**os.environ, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when}
    subprocess.run(["git", "commit", "-m", message], check=True, env=env)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true",
                    help="commit each submission (dated when you solved it) and push")
    args = ap.parse_args()

    state = json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {"seen": [], "problems": {}}
    seen = set(state["seen"])
    problems = state["problems"]

    s = make_session()
    new_subs = list(fetch_accepted(s, seen))
    print(f"{len(new_subs)} new accepted submission(s).")

    saved = []
    for sub in reversed(new_subs):  # oldest first, so commits are chronological
        key = f"{sub['title_slug']}:{sub['lang']}"
        try:
            q = fetch_question(s, sub["title_slug"])
        except Exception as e:  # keep going; retry next run
            print(f"  skip {sub['title_slug']}: {e}")
            continue
        info = save_problem(q, sub)
        problems[key] = info
        seen.add(sub["id"])
        saved.append(sub)
        print(f"  saved {info['id']}. {info['title']} ({info['lang']})")
        if args.push:
            git_commit(f"Solve {info['id']}. {info['title']} ({info['lang']})",
                       [info["folder"]], sub["timestamp"])
        time.sleep(DELAY)

    STATE_FILE.write_text(json.dumps({"seen": sorted(seen), "problems": problems}, indent=1))

    if saved:
        write_root_readme(problems)
        if args.push:
            # Dated at the newest solve, so no commit claims activity that didn't happen.
            git_commit("Update README and sync state",
                       ["README.md", STATE_FILE.as_posix()], saved[-1]["timestamp"])
            subprocess.run(["git", "push"], check=True)
    else:
        print("Nothing new to commit.")


if __name__ == "__main__":
    main()

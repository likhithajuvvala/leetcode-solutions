class Solution {
    public boolean isAnagram(String s, String t) {
      if (s.length() != t.length()) return false;

        int[] count = new int[26];

        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++; // letter in s: +1
            count[t.charAt(i) - 'a']--; // letter in t: -1
        }

        for (int c : count) {
            if (c != 0) return false;
        }

        return true;
    }
}
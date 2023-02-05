class Solution {
    public List<Integer> findAnagrams(String s, String p) {
         int CHARACTERS = 256;
		int k = p.length();
		char[] sArr = new char[CHARACTERS];
		char[] pArr = new char[CHARACTERS];
		for (int i = 0; i < p.length(); i++) {
			pArr[p.charAt(i)]++;
		}
		int i = 0;
		int j = 0;
        List<Integer> list = new ArrayList<>();
		while (j < s.length()) {
			sArr[s.charAt(j)]++;
			if (j - i + 1 >= k) {
				if (Arrays.equals(pArr, sArr))
					list.add(i);
				sArr[s.charAt(i)]--;
				i++;
			}
			j++;
		}
		return list;
    }
}
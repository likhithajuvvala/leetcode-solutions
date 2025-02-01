class Solution {
    public String findValidPair(String s) {
        int[] freq = new int[10];  // 0-9 digits
        for (char c : s.toCharArray()) {
            freq[c - '0']++;
        }
        
        // Check each adjacent pair
        for (int i = 0; i < s.length() - 1; i++) {
            int first = s.charAt(i) - '0';
            int second = s.charAt(i + 1) - '0';
            
            // Check conditions:
            // 1. Different digits
            // 2. First digit appears exactly its value times
            // 3. Second digit appears exactly its value times
            if (first != second && 
                freq[first] == first && 
                freq[second] == second) {
                return s.substring(i, i + 2);
            }
        }
        
        return "";
    }
}
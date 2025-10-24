class Solution {
    private boolean isBalanced(int num) {
        int[] count = new int[10];
        String s = Integer.toString(num);
        for (int i = 0; i < s.length(); i++) {
            int d = s.charAt(i) - '0';
            count[d]++;
        }
        for (int i = 0; i < s.length(); i++) {
            int d = s.charAt(i) - '0';
            if (d == 0 || count[d] != d) return false;
        }
        return true;
    }
    public int nextBeautifulNumber(int n) {
        for (int i = n + 1; ; i++) {
            if (isBalanced(i)) return i;
        }
    }
}
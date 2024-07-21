class Solution {
    public int minChanges(int n, int k) {
       
        k ^= n;
        int cnt = Integer.bitCount(k);
        k &= n;
        return cnt == Integer.bitCount(k) ? cnt : -1;
   
    }
}
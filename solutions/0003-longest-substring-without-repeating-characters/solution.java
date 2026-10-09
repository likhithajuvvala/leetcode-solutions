class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character>st = new HashSet<>();
        int best=0;
        int l=0;
        for(int i=0;i<s.length();i++){
            char c= s.charAt(i);
            while(st.contains(c)){
                st.remove(s.charAt(l));
                l++;
            }
            st.add(c);
            best = Math.max(best,i-l+1);
        }
        return best;
    }
}
class Solution {
    public int lengthOfLongestSubstring(String s) {
       if(s.length()==0){
        return 0;
       } 
        Set<Character>st=new HashSet<>();
        int l = Integer.MIN_VALUE;
        int left=0,right=0;
        for(right=0;right<s.length();right++){
            if(st.contains(s.charAt(right))){
                while(left<right && st.contains(s.charAt(right))){
                    st.remove(s.charAt(left));
                    left++;
                }
            }
            st.add(s.charAt(right));
            l=Math.max(l,right-left+1);

        }
        return l;
    }
}
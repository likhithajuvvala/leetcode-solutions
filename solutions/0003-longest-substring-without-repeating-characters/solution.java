class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left=0,right=0,len=0;
        Map<Character,Integer>m=new HashMap<>();
        while(right<s.length()){
            if(m.containsKey(s.charAt(right))){
                left = Math.max(m.get(s.charAt(right))+1,left);
            }
            m.put(s.charAt(right),right);
            len=Math.max(len,right-left+1);
            right++;
        }
        return len;

    }
}
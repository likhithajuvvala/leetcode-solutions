class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        int[] need = new int[26];
        int[] window = new int[26];
        for(int i=0;i<s1.length();i++){
            need[s1.charAt(i)-'a']++;
        }
        int k = s1.length();
        for(int r=0;r<s2.length();r++){
            window[s2.charAt(r)-'a']++;
                if(r>=k){
                    window[s2.charAt(r-k)-'a']--;  
                    } //l=r-k+1 and one step reduce so (r-k+1)-1
                  if(Arrays.equals(need, window)) return true;
            
        }
        return false;
    }
}
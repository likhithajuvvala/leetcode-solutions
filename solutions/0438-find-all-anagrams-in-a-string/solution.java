class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList<>();
        if(p.length()>s.length()){
            return result;
        }
        int[] need = new int[26];
        int[] window = new int[26];

        for(int i=0;i<p.length();i++){
           need[p.charAt(i)-'a']++;
        }
        int k=p.length();
        for(int r=0;r<s.length();r++){
            window[s.charAt(r)-'a']++;
            if(r>=k){
                window[s.charAt(r-k)-'a']--;
            }
            if(Arrays.equals(need,window)){
                result.add(r-k+1);
            }
        }
        return result;
    }
}
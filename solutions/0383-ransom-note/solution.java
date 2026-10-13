class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        String s1= ransomNote;
        String s2= magazine;
        if(s1.length()>s2.length()){
            return false;
        }
        int count[] =new int[26];
        for(int i=0;i<s2.length();i++){
            count[s2.charAt(i)-'a']++;
        }
        for(int i=0;i<s1.length();i++){
            int idx = s1.charAt(i)-'a';
        if(count[idx]==0) return false;
        else {
            count[idx]--;
        }
        }
        return true;
    }
}
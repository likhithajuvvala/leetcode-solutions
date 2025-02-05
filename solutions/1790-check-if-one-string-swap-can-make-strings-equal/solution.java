class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if(s1.equals(s2)) return true;
        int mismatch =0;
        List<Character>res=new ArrayList<>();
        int i=0;
        while(i<s1.length()){
            if(s1.charAt(i)!=s2.charAt(i)){
                res.add(s1.charAt(i));
                res.add(s2.charAt(i));
                mismatch++;
            }
            i++;
        }
        if(res.size()==4){
            return(res.get(0) == res.get(3) && res.get(1) == res.get(2));
     
       }
       return false;
    }
}
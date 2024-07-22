class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        int n= names.length;
        String result[] = new String[n];
        HashMap<Integer,String>hm = new HashMap<>();
        for(int i=0;i<n;i++){
            hm.put(heights[i],names[i]);
        }
        Arrays.sort(heights);
        int a =0;
        for(int i=n-1;i>=0;i--){
            result[a]=hm.get(heights[i]);
            a++;
        }
        return result;
    }
}
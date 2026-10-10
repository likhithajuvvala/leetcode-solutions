class Solution {
    public int totalFruit(int[] fruits) {
        int l=0;
        int best =0;
        Map<Integer, Integer> count = new HashMap<>();
        for(int r=0;r<fruits.length;r++){
            count.put(fruits[r], count.getOrDefault(fruits[r],0)+1);
            while(count.size()>2){
                count.put(fruits[l],count.get(fruits[l])-1);
                if(count.get(fruits[l])==0){
                    count.remove(fruits[l]);
                }
                l++;
            }
            best = Math.max(best,r-l+1);
        }
        return best;
    }
}
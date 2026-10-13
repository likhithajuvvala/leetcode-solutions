class Solution {
    public int maxProfit(int[] prices) {
        int l=0;
        int best =0;
        for(int r=0;r<prices.length;r++){
           if(prices[r]<prices[l]){
            l=r;
           }
           else{
            best=Math.max(best,prices[r]-prices[l]);
           }
        }
        return best;
    }
}
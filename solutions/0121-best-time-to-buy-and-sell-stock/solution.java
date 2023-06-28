class Solution {
    public int maxProfit(int[] prices) {
      int min=Integer.MAX_VALUE;
      int maxpro=0;
      int max=0;
      for(int i=0;i<prices.length;i++){
          if(prices[i]<min){
              min=prices[i];
          }
          max=prices[i]-min;
          if(maxpro<max)
          maxpro=max;
      }  
    
    return maxpro;
}
}
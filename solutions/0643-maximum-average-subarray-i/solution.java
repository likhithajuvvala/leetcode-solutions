class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double avg = -Double.MAX_VALUE;
        int sum =0;

        for(int r=0;r<nums.length;r++){
             sum += nums[r];

            if(r>=k-1){
                avg = Math.max(avg, (double)sum/k);
                sum-=nums[r-k+1];
            }
        }
        return avg;
    }
}
class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0;
        int minlength=0;
        int sum=0;
        for(int r=0;r<nums.length;r++){
            sum+=nums[r];
            while(sum>=target){
                int length = r-l+1;
                if(minlength==0||length<minlength){
                    minlength = length;
                }
                sum-=nums[l];
                l++;
            }
        }
        return minlength;
    }
}
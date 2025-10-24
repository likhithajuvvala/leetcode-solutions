class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int sum=0,minlen=Integer.MAX_VALUE,left=0;
        for(int r=0;r<nums.length;r++){
             sum=sum+nums[r];
            while(sum>=target){
            minlen=Math.min(minlen,r-left+1);
            sum=sum-nums[left];
            left++;
            }
        }
        return (minlen==Integer.MAX_VALUE)?0:minlen;
        
    }
}
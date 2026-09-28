class Solution {
    public void rotate(int[] nums, int k) {
        k%=nums.length;
        int n=nums.length;
        reverseNums(nums,0,n-1);
        reverseNums(nums,0,k-1);
        reverseNums(nums,k,n-1);
    }
        public void reverseNums(int[] nums,int start, int end){
            while(start<end){
                int temp = nums[start];
                nums[start]=nums[end];
                nums[end]=temp;
                start++;
                end--;
            }
        }
}
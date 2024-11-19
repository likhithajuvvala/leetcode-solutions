class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
         HashSet<Integer>hs=new HashSet<>();
         int i=0,j=0;
         long max=0,sum=0;
         while(j<nums.length){
            int temp=nums[j];
            while(hs.contains(temp)){
                hs.remove(nums[i]);
                max=max-nums[i];
                i++;
            }
            max=max+temp;
            if((j-i+1)==k){
                sum=Math.max(sum,max);
                max=max-nums[i];
                hs.remove(nums[i]);
                i++;
            }
            hs.add(temp);
            j++;
         }
         return sum;
    }
}
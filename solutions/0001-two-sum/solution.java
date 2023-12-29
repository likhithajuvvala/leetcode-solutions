class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer>mpp = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int num=nums[i];
            int diff=target-num;
            if(mpp.containsKey(diff)){
                return new int[]{i,mpp.get(diff)};
            }
            mpp.put(nums[i],i);
        }
        return new int[]{};
    }
}
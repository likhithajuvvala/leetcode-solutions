class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int target=0;
        Arrays.sort(nums);
        Set<List<Integer>>st = new HashSet<>();
        List<List<Integer>>ans = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            int j=i+1;
            int k=nums.length-1;
            while(j<k){
                int sum = nums[i]+nums[j]+nums[k];
                if(sum<target){
                    j++;
                }
                else if(sum>0){
                    k--;
                }
                else{
                    st.add(Arrays.asList(nums[i],nums[j],nums[k]));
                    j++;
                    k--;
                }
            }
        }
        ans.addAll(st);
        return ans;
    }
}
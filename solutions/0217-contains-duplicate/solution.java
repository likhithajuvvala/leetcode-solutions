class Solution {
    public boolean containsDuplicate(int[] nums) {
      /* 
      SOrting
      
       Arrays.sort(nums);
        for(int i =1;i<nums.length;i++){
            if(nums[i]==nums[i-1]){
                return true;
            }
          
        }
          return false;*/

          Set<Integer>st= new HashSet<>();
          for(int i:nums){
            if(st.contains(i)){
                return true;
            }
            st.add(i);
          }
        return false;
    }
}
class Solution {
    public int majorityElement(int[] nums) {
        int cand=0;
        int points=0;
        for(int i=0;i<nums.length;i++){
            if(points==0){
                cand=nums[i];
            }
            if(cand==nums[i]){
                points++;
            }
            else{
                points--;
            }
        }
        return cand;
    }
}
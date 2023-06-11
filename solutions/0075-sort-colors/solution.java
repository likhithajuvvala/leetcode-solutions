class Solution {
    public void sortColors(int[] nums) {
       int l = 0;
        int m = 0;
        int h = nums.length-1;
        //O(N) only
        while(m<=h){
            if(nums[m] == 0){
                //Swap l and m 
                int temp = nums[l];
                nums[l] = nums[m];
                nums[m] = temp;
                l++;
                m++;
            } else if(nums[m]==1){
                m++;
            } else{
                //Swap m and h 
                int temp = nums[m];
                nums[m] = nums[h];
                nums[h] = temp;
                h--;
               }
               
           }
       } 
    }

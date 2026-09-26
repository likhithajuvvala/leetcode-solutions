class Solution {
    public int removeDuplicates(int[] nums) {
         if (nums.length == 0) return 0;

        int count = 0; // count = index of last unique element kept
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[count]) {   // compare to last kept value
                count++;
                nums[count] = nums[i];
            }
            // else: duplicate, do nothing (no need for explicit continue)
        }
        return count + 1;
    }
}
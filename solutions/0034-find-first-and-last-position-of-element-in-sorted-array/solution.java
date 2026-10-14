class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = position(nums,target);
        if (first == nums.length || nums[first] != target) {
        return new int[] { -1, -1 };
    }
    int last = position(nums, target + 1) - 1;
    return new int[] { first, last };
}

// exactly your 35 code
private int position(int[] nums, int target) {
    int left = 0, right = nums.length - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) right = mid - 1;   // only change from 35
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return left;
}
}
class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int total = nums[0];
        int curMax = nums[0], bestMax = nums[0];
        int curMin = nums[0], bestMin = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int x = nums[i];
            total = total + x;

            // BIGGEST stretch (your exact logic)
            if (curMax < 0) {
                curMax = x;
            } else {
                curMax = curMax + x;
            }
            if (curMax > bestMax) {
                bestMax = curMax;
            }

            // SMALLEST stretch (the mirror image)
            if (curMin > 0) {
                curMin = x;
            } else {
                curMin = curMin + x;
            }
            if (curMin < bestMin) {
                bestMin = curMin;
            }
        }

        if (bestMax < 0) {
            return bestMax;
        }
        return Math.max(bestMax, total - bestMin);
    }
}
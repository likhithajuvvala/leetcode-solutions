class Solution {
    public int longestConsecutive(int[] nums) {
        Arrays.sort(nums);
        if(nums.length==0) return 0;
        int last_number = Integer.MIN_VALUE;
        int cnt = 0;
        int longest = 1;
        for(int num:nums){
            if(num-1 == last_number){
                cnt++;
                last_number=num;
            } else if(num!=last_number){
                cnt=1;
                last_number=num;
            }
            longest=Math.max(longest,cnt);
        }
        return longest;
    }
}
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int l1 = m-1;
        int l2 = n-1;
        for(int k = n+m-1;k>=0;k--){
            if(l2<0){
                break;
            }
            if(l1>=0&&nums1[l1]>nums2[l2]){
                nums1[k]=nums1[l1];
                l1--;
            }
            else{
                nums1[k]=nums2[l2];
                l2--;
            }
        }
    }
}
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int count=0;
        do{
            if(count==1){
                break;
            }
            count++;
        }while(next_permutation(nums.begin(),nums.end()));
    }
};
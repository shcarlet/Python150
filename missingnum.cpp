class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int missing=0;
        for(int i = 1;i<nums.size();i++)
        {
            if(nums[i]!=nums[i-1]+1)
            {
                return nums[i]-1;
            }
        }
        if(n!=nums[n-1])
        {
            return n;
        }
        else
        {
            return 0;
        }
    }
};

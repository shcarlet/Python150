class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left=0,sum=0;
        int minlen=numeric_limits<int>::max();
        for(int r=0;r<nums.size();r++)
        {
            sum=sum+nums[r];
            while(sum>=target)
            {
                if(minlen>r-left+1)
                {
                    minlen=r-left+1;
                }
                sum=sum-nums[left];
                left++;
            }
        }
        return minlen!=numeric_limits<int>::max()?minlen:0;
    }
};

class Solution(object):
    def minSubArrayLen(self, target, nums):
        minlen=float("inf")
        left=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            while sum>=target:
                if minlen>i-left+1:
                    minlen=i-left+1
                sum-=nums[left]
                left=left+1
        return minlen if minlen!=float("inf") else 0
        

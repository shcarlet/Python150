class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i,v in enumerate(nums):
            if i!=v:
                return v-1
            if len(nums)-1==v:
                return v+1
        

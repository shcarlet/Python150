class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for index,value in enumerate(nums):
            if index!=value:
                return value-1
            if len(nums)-1==value:
                return value+1
        

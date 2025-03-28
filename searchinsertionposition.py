class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)
        if target>nums[high-1]:
            return high
        while low<=high:
            mid=(low+high)/2
            if target==nums[mid]:
                return mid
            if target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return low

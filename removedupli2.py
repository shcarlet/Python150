class Solution(object):
    def removeDuplicates(self, nums):
        index=2
        if len(nums)<=2:
            return len(nums)
        for i in range(2,len(nums)):
            if nums[i]!=nums[index-2]:
                nums[index]=nums[i]
                index+=1
        return index

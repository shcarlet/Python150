class Solution(object):
    def findDisappearedNumbers(self, nums):
        set1 = set(nums)
        res = []
        for i in range(1,len(nums)+1):
            if i not in set1:
                res.append(i)
        return res

class Solution(object):
    def longestConsecutive(self, nums):
        mp_set = set(nums)
        res=0
        for n in mp_set:
            if n-1 not in mp_set:
                count=1
                while n+count in mp_set:
                    count=count+1
                res=max(res,count)
        return res

        

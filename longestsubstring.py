class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s1=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in s1:
                s1.remove(s[l])
                l=l+1
            s1.add(s[i])
            res=max(res,i-l+1)
        return res 
        

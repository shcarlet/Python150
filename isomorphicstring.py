class Solution(object):
    def isIsomorphic(self, s, t):
        mpnum={}
        mp2num={}

        for i in range(len(s)):
            if s[i] not in mpnum:
                mpnum[s[i]]=i
            if t[i] not in mp2num:
                mp2num[t[i]]=i
            if mpnum[s[i]]!=mp2num[t[i]]:
                return False
        return True
        
        

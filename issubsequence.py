class Solution(object):
    def isSubsequence(self, s, t):
       sp=tp=0
       while sp<len(s) and tp<len(t):
        if s[sp]==t[tp]:
            sp=sp+1
        tp=tp+1
    
       return sp==len(s)

         

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        s1={}
        for char in s:
            s1[char]=s1.get(char,0)+1
        for char in t:
            if char not in s1 or s1[char]==0:
                return False
            s1[char]-=1
        
        return True

       
        

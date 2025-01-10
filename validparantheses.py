class Solution(object):
    def isValid(self, s):
        s1=[]
        for i in range(len(s)):
            if s[i]=='[' or s[i]=='{' or s[i]=='(':
                s1.append(s[i])
            elif len(s1)==0:
                return False
            elif (s[i]==']' and s1[-1]=='[') or (s[i]=='}' and s1[-1]=='{') or (s[i]==')' and s1[-1]=='('):
                s1.pop()
            else:
                return False
        if len(s1)==0:
            return True
        else:
            return False

        

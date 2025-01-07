class Solution(object):
    def maxArea(self, height):
       l=0
       r=len(height)-1
       res=0
       while(l<r):
        minh=min(height[l],height[r])
        area=minh*(r-l)
        res=max(res,area)
        if height[l]<=height[r]:
            l=l+1
        else:
            r=r-1
       return res
    

        

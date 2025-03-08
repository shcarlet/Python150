class Solution(object):
    def longestMountain(self, arr):
        res=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                l=h=i
                while l>0 and arr[l]>arr[l-1]:
                    l=l-1
                while h+1<len(arr) and arr[h]>arr[h+1]:
                    h+=1
                res=max(res,h-l+1)
        return res

class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        mindiff=float('inf')
        for i in range(len(arr)-1):
            mindiff=min(mindiff,arr[i+1]-arr[i])
        j=0
        res=[]
        while j<len(arr)-1:
            if arr[j+1]-arr[j]==mindiff:
                res.append([arr[j],arr[j+1]])
            j=j+1
        return res

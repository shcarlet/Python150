class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        k=0
        for i in range(1,len(intervals)):
            if intervals[k][1]>=intervals[i][0]:
                intervals[k][1]=max(intervals[k][1],intervals[i][1])
            else:
                k+=1
                intervals[k]=intervals[i]
        return intervals[:k+1]
        

class Solution(object):
    def findKthLargest(self, nums, k):
        minh = []
        for num in nums:
            heapq.heappush(minh,num)
            if len(minh)>k:
                heapq.heappop(minh)
        return minh[0]

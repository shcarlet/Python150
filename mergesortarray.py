class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l=m-1
        j=n-1
        
        i=m+n-1
       
        while l>=0 and j>=0:
            if nums1[l]>=nums2[j]:
                nums1[i]=nums1[l]
                l=l-1
            else:
                nums1[i]=nums2[j]
                j=j-1
            i=i-1
        while j>=0:
            nums1[i]=nums2[j]
            j=j-1
            i=i-1
        

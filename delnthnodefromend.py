# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        #FAST PTR SLOW PTR
        res = ListNode(0,head)
        dummy = res
        for i in range(n):
            head=head.next
        while head:
            head=head.next
            dummy=dummy.next
        dummy.next=dummy.next.next
        return res.next
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        res=dummy
        total=0
        carry=0
        while l1 or l2 or carry:
            total=carry
            if l1:
                total+=l1.val
                l1=l1.next
            if l2:
                total+=l2.val
                l2=l2.next
            n=total%10
            carry=total/10
            dummy.next=ListNode(n)
            dummy=dummy.next
        return res.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return  head
        fast = head
        if fast.next != None:
            head = fast.next
        while fast != None:
            first = fast
            fast = fast.next
            second = fast
            if fast != None:
                fast = fast.next
                second.next = first
            if fast != None and fast.next != None:
                first.next = fast.next
            else:
                first.next = fast
        return head
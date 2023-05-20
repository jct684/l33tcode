# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #number of nodes? [0. 10^4]
        #value range of nodes? [-10^5, 10^5]
        #are the node values unique? no
        #time complexity O(n)
        #space complexity O(1)
        slow = head
        fast = head
        while(slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                return True
        return False
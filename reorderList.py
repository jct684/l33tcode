# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #number of nodes [1, 50000]
        #possible values [1, 1000]
        #time complexity O(n)
        #space complexity O(1)
        # 1 2 3 4 5 6
        # 1 6 2 3 4 5
        # 1 6 2 5 3 4
        #slow and fast to reverse the latter half
        #alternate between the two remaining linked lists
        if(head.next == None or head.next.next == None):
            return head
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        reverse_node = slow.next
        reverse_next_node = reverse_node.next
        reverse_node.next = None
        while(reverse_next_node):
            temp = reverse_next_node.next
            reverse_next_node.next = reverse_node
            reverse_node = reverse_next_node
            reverse_next_node = temp

        slow.next = None
        curr_node = head
        next_node = head.next
        while(reverse_node):
            curr_node.next = reverse_node
            new_reverse_node = reverse_node.next
            reverse_node.next = next_node
            curr_node = next_node
            next_node = next_node.next
            reverse_node = new_reverse_node
        return head
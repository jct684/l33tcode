# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #return iterative_solution(head)
        return recursive_solution(head)

def iterative_solution(head):
    #time complexity O(n)
    #space complexity O(1)
    curr_node = head
    if(curr_node):
        next_node = curr_node.next
        curr_node.next = None
        while(next_node):
            next_next_node = next_node.next
            next_node.next = curr_node
            curr_node = next_node
            next_node = next_next_node
    return curr_node

def recursive_solution(head):
    #time complexity O(n)
    #space complexity O(n)
    if(head == None or head.next == None):
        return head
    new_head = recursive_solution(head.next)
    head.next.next = head
    head.next = None
    return new_head
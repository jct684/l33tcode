# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return add_two_numbers(l1, l2)

def add_two_numbers(l1, l2):
    remainder = 0
    current_sum = l1.val + l2.val
    if current_sum > 9:
        remainder = 1
        current_sum = current_sum % 10
    head = ListNode(current_sum)
    ans = head
    l1 = l1.next
    l2 = l2.next
    while(l1 != None or l2 != None):
        if l1 == None:
            current_sum = l2.val + remainder
            ans, remainder = add_new_node(current_sum, ans)
            l2 = l2.next
        elif l2 == None:
            current_sum = l1.val + remainder
            ans, remainder = add_new_node(current_sum, ans)
            l1 = l1.next
        else:
            current_sum = l1.val + l2.val + remainder
            ans, remainder = add_new_node(current_sum, ans)
            l1 = l1.next
            l2 = l2.next
    if remainder == 1:
        ans.next = ListNode(1)
    return head

def add_new_node(current_sum, ans):
    if current_sum > 9:
        remainder = 1
        current_sum = current_sum % 10
        ans.next = ListNode(current_sum)
    else:
        remainder = 0
        ans.next = ListNode(current_sum)
    return ans.next, remainder
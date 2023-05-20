# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #time complexity O(n log k) where n is number of nodes and k is number of levels to be merged
        #space complexity O(1)
        if lists == []:
            return None
        while len(lists) > 1:
            new_lists = []
            for i in range(1, len(lists), 2):
                new_lists.append(merge2Lists(lists[i-1], lists[i]))
            if(len(lists) % 2 == 1):
                new_lists.append(lists[-1])
            lists = new_lists
        return lists[0]

def merge2Lists(l1, l2):
    if (l2 == None):
        return l1
    elif(l1 == None):
        return l2
    else:
        dummy_head = ListNode()
        curr_node = dummy_head
        while(l1 and l2):
            if(l1.val < l2.val):
                curr_node.next = l1
                l1 = l1.next
            else:
                curr_node.next = l2
                l2 = l2.next
            curr_node = curr_node.next
        if(l1):
            curr_node.next = l1
        if(l2):
            curr_node.next = l2
        return dummy_head.next
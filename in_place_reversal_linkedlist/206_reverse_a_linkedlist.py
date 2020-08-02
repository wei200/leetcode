# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # in place solution
        # O(N)
        # O(1)
        
        current = head
        previous = None
        next = None
        
        while current is not None:
            tempnext = current.next # temporarily store the next node
            current.next = previous  # reverse the current node
            previous = current # before moving to hte next node, point previous to the current node
            current = tempnext # move on the next node
            
        return previous
            
            
        

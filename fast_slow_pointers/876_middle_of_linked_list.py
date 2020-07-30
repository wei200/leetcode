# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # fast and slow pointers
        # O(N)
        # O(1)
        
        #We can use the Fast & Slow pointers method such that the fast pointer is always twice the nodes ahead of the slow pointer. 
        # This way, when the fast pointer reaches the end of the LinkedList, the slow pointer will be pointing at the middle node.
        
        fast = head
        slow = head 
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

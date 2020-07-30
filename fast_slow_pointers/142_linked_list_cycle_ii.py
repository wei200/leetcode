# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # O(N)
        # O(1)
        fast = head
        slow = head
        cycle_length = 0
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: # found the cycle
                cycle_length = self.calculate_cycle_length(slow)
                break
        if cycle_length == 0:
            return None
        else:
            return self.find_start(head, cycle_length)
            
        
    def calculate_cycle_length(self,slow):
        current = slow
        cycle_length = 0
        while True:
            current = current.next
            cycle_length += 1
            if current == slow:
                break
        return cycle_length
    
    def find_start(self, head, cycle_length):
        pointer1 = head
        pointer2 = head
        # move pointer2 ahead 'cycle_length' nodes
        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1
        # increment both pointers until they meet at the start of the cycle
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
    
        
        
            
        

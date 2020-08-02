# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        
        # In-place reversal
        # O(N)
        # O(1)
        # 1. Skip the first m - 1 nodes, to reach the node at position m
        # 2. remember the ndoe at pos m-1 to be used later to connect with reversed sub-list
        # 3. reverse the sublist
        # 4. connect the m-1 and n + 1 ndoes to the reversed sub-list
        
        if m == n:
            return head
        current = head
        previous = None
        i = 0
        # skip the fist m - 1 nodes
        while current is not None and i < m - 1:
            previous = current
            current = current.next
            i += 1
            
        last_node_of_first_part = previous
        last_node_of_sub_list = current
        #temp_next = None # tempnext is used temporarily store the next node
        i = 0
        # reverse nodes between m and n
        while current is not None and i < n - m + 1:
            temp_next = current.next
            current.next = previous
            previous = current
            current = temp_next
            i += 1
        
        # connect with the first part, the sublist is prevous->xxx->current. If [m,n] covers the entire linked list, last node of first part is None, previous will be the head
        if last_node_of_first_part is not None:
            last_node_of_first_part.next = previous
            
        else:
            head = previous
            
        # connect wit the first part
        last_node_of_sub_list.next = current
        
        return head
        
            
            
            
            
        
        

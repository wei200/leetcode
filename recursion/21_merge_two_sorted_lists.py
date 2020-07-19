
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # recursion 
        # Time: O(m + n) since each call increase the pointer by 1 location in
        # either l1 or l2
        # Space: O(m + n), The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached, so n + mn+m stack frames consume O(n + m)O(n+m) space
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val <= l2.val:
            pt = l1
            pt.next = self.mergeTwoLists(l1.next,l2)
        else:
            pt = l2
            pt.next = self.mergeTwoLists(l1,l2.next)
            
        return pt
        
        # interation approach, later for next round
        

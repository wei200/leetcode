# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # O(N * Log K), K is the size of input array
        # O(K) keep the min heap
        h = []
        
        # put the root of each list in the min heap
        for lst in lists:
            if lst:
                heapq.heappush(h, (lst.val, lst))
        
        # take the top/smallest element from the min heap and add it to the result
        rhead = rtail = ListNode(0)
        
        while h:
            _, n = heapq.heappop(h)
            # print("n",n)
            # print("n.next",n.next)
            rtail.next = n
            # print("rtail.next",rtail.next)
            # print("rtail",rtail)
            rtail = rtail.next
            # print("rtail",rtail)
            # print("___________")
            if n.next:
                heapq.heappush(h, (n.next.val, n.next))
                
        return rhead.next

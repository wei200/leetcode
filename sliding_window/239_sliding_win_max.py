class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # sliding window, only save index of the element to the queue
        # base check
        if k == 1:
            return nums
        # double-ended queue
        queue = deque()
        result = []
        
        # only add max value of the first k elements
        for i in range(k):
            while len(queue) != 0:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            queue.append(i)

        for i in range(k, len(nums)):
            result.append(nums[queue[0]])
            if queue[0] < i-k+1: # if left most is still in the range of window k
                queue.popleft()
            
            while len(queue) != 0:
                if nums[i] > nums[queue[-1]]:
                    queue.pop()
                else:
                    break
            # the leftmost of the queue stores the index of max val
            queue.append(i)
          

        result.append(nums[queue[0]])        
        return result
                
                
            

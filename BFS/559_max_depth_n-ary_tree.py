"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is None:
            return 0
        result = []
        queue = deque()
        queue.append(root)
        max_depth = 0
        while queue:
            max_depth += 1
            level_size = len(queue)
            for i in range(level_size):
                
                current_node = queue.popleft()
                for j in current_node.children:
                    if j:
                        queue.append(j)
                        
        return max_depth
                

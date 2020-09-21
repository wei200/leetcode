# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        # defaultdict(list) + BFS
        # O(N) + O(NlogN) (sorted)
        # O(N)
        
        if root is None:
            return root
        queue = deque()
        # append(currentnode,column) to the double ended queue
        queue.append((root,0))
        column_map = collections.defaultdict(list)
        
        while queue:
            current_node, column = queue.popleft()
            if current_node:
                column_map[column].append(current_node.val)
            if current_node.left:
                queue.append((current_node.left, column-1))
            if current_node.right:
                queue.append((current_node.right, column+1))
        # column_map:{0: [3, 15], 1: [20], 2: [7], -1: [9]})
        # return  [[9], [3, 15], [20], [7]] sorted by the key

        return [column_map[column] for column in sorted(column_map)] 
        
                
                

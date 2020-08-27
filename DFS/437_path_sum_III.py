# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        # DFS
        # see notes for time and space complexity
        return self.find_counts(root,sum,[])
    
    
    def find_counts(self,current_node,sum,current_path):
        
        if current_node is None:
            return 0
        
        # add the current node to the path
        current_path.append(current_node.val)
        count = 0
        path_sum = 0
        
        # find the sums of all sub-paths in teh current path list
        for i in range(len(current_path)-1,-1,-1):
            path_sum += current_path[i]
            # if the sum of any sub-path is equal to the target sum we increment the path count
            if path_sum == sum:
                count += 1
                
        # traverse the left tree
        count += self.find_counts(current_node.left,sum,current_path)
        # travese the right tree
        count += self.find_counts(current_node.right,sum,current_path)
        
        # remove the current node for backtrack
        # we need to remove the current node while goign up the recursive call stack
        del current_path[-1]
        
        return count

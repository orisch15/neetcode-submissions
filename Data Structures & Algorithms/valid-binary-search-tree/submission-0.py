# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        #we will use dfs to check if each node statsfies the range
        #we say that node is valid if it is between low and high
        def valid(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float('-inf'), float('inf'))

            

        
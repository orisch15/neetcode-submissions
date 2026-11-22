# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            # the hight that will be returned is considered with the edge beetween the parent node. so its actually more like the real hight + 1
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            # the global value that sums up the connected paths
            res = max(res, right + left)
            # the return value of the next hight without connecting
            return 1 + max(right, left)
        dfs(root)
        # note thet we dont return dfs() because it returns the hight wich
        return res
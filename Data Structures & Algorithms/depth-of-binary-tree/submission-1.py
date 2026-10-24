# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #DFS - simple recursion to find the max hight
    #for a given root, we will ask it two sons who is taller?
    #base case - empty node - return 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.rec_d(root)

    def rec_d (self, root):
        if not root:
            return 0

        left_h = self.rec_d(root.left)
        right_h = self.rec_d(root.right)
        return max(left_h, right_h) + 1
        
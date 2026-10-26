# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS - add the nodes in-order to an array using bst
        #the array will be sorted and we will return arr[k-1]
        arr = []
        def rec ( node):
            if not node:
                return None
            rec(node.left)
            arr.append(node.val)
            rec(node.right)

        rec(root)
        return arr[k-1]
        
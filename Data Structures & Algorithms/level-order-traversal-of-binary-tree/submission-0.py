# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #we remember that BFS does exacly that using a queue
        #we will check how ,any nodes in each level by calculating len of q 
        #at the start of a new iteration
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        while q:
            l = len(q)
            arr = []
            for _ in range(l):
                node = q.popleft()
                arr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(arr)
        return res       
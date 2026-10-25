# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #use BFS alg to travel across all of the nodes in root

        q = [root]
        res = False
        while q:
            node = q.pop()
            if node:
                if node.val == subRoot.val:
                    if self.same_tree(node, subRoot):
                        res = True
                q.append(node.left)
                q.append(node.right)
        
        return res
    

    def same_tree(self, p, q):
        #DFS alg for determining if two trees are the same
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #we will dfs to build the tree.
        #the recursion will find root, attach him left and right using the
        #rec step' and then return him/ base case: root == none
        
        #global index to track the pre order arrays root. it will add 1 every step
        #so when we will enter the right subtree the number of steps will match the root
        self.preindex = 0
        indices = {}
        for i in range(len(inorder)):
            indices[inorder[i]] = i

        
        def dfs(l, r):
            #base case
            if l>r:
                return None
            #look for the root in the map in O(1)
            root_val = preorder[self.preindex]
            root = TreeNode(root_val)
            mid = indices[root_val]
            #t
            self.preindex += 1

            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, len(inorder) - 1)



            
            










        
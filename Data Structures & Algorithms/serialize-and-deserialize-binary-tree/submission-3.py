# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #dfs - pre order traversal with "n" to mark empty nodes to remember the edges

        # it has to be an array to capture multy digit numbers
        res = []

        def dfs(node):
            if not node:
                #to mark none nodes
                res.append('N')
                return None
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(',')
        self.index = 0
        def dfs():
            if res[self.index] == 'N':
                self.index += 1
                return None
            root = TreeNode(int(res[self.index]))
            self.index += 1
            root.left = dfs()
            root.right = dfs()

            return root
        return dfs()

        









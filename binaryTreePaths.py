# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        
        if root is None:
            return paths
        
        def dfs(root, path):
            path += str(root.val)
            
            if root.left is None and root.right is None:
                paths.append(path)
                
            if root.left:
                dfs(root.left, path + "->")
                
            if root.right:
                dfs(root.right, path + "->")
            

        dfs(root, "")
        return paths

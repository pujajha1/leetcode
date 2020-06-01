#https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def recur(root):
            if root is None:
                return 
            root.left,root.right=root.right,root.left
            recur(root.left)
            recur(root.right)
            return root
        recur(root)
        return root

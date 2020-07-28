https://leetcode.com/problems/maximum-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        maximum=max(nums)
        split_index=nums.index(maximum)
        node=TreeNode(maximum)
        if len(nums[:split_index]):
            node.left=self.constructMaximumBinaryTree(nums[:split_index])
        if len(nums[split_index+1:]):
            node.right=self.constructMaximumBinaryTree(nums[split_index+1:])
            
        return node

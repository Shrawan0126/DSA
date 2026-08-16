# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
            if not root.left and not root.right:
                return bool(root.val)
            
            left = self.evaluateTree(root.left)
            right = self.evaluateTree(root.right)

            node = root.val
            if node==2:
                root.val = left or right
            else :
                root.val = left and right

            return root.val
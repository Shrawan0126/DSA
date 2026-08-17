# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root: TreeNode):
        if root == None:
            return 

        self.inorder(root.left)
        self.temp.right = TreeNode(root.val)
        self.temp = self.temp.right

        self.inorder(root.right)
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # inorder : 1 2 3 4 5 6 7 8 9
        # now contruct the tree using inorder traversal
        head = TreeNode(0)
        self.temp = head
        self.inorder(root)

        return head.right



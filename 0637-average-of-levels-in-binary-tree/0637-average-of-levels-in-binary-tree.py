# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        q = []
        temp  = []

        q.append(root)
        curr_level = 0

        while q:
            len_q = len(q)
            temp.append([])

            for _ in range(len_q):
                node = q.pop(0)
                temp[curr_level].append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            curr_level += 1
        
        ans = []
        for i in range(0,len(temp)):
            ans.append( sum(temp[i]) / len(temp[i]) )

        return ans
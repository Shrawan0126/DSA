# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])

        while q:
            len_q = len(q)
            level_sum = 0

            for _ in range(len_q):
                node = q.popleft()
                level_sum += node.val

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            ans.append(level_sum / len_q)      

        return ans
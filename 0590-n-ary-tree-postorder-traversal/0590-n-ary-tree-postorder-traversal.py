"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def post(self, root: 'Node', arr : List[int]):
        if root == None:
            return

        for child in root.children:
            self.post(child, arr)
        
        arr.append(root.val)
       

    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        self.post(root, arr)

        return arr
        
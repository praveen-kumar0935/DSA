# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def h(n):
            if not n: return None
            lt=h(n.left); rt=h(n.right)
            if n.left:
                (lt.right if lt else None) and setattr(lt,'right',lt.right)
                if lt: lt.right=n.right
                n.right=n.left; n.left=None
            return rt or lt or n
        h(root)
        """
        Do not return anything, modify root in-place instead.
        """
        
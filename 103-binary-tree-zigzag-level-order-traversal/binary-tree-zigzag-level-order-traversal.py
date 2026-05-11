# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque([root])
        left_to_right = True
        while q:
            level_size = len(q)
            level_vals = deque()
            for _ in range(level_size):
                node = q.popleft()
                if left_to_right:
                    level_vals.append(node.val)
                else:
                    level_vals.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(list(level_vals))
            left_to_right = not left_to_right
        return result

        
        
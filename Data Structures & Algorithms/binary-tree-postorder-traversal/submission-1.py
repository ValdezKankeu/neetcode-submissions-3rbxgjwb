# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visted = [False]
        res = []

        while stack:
            curr = stack.pop()
            v = visted.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visted.append(True)
                    stack.append(curr.right)
                    visted.append(False)
                    stack.append(curr.left)
                    visted.append(False)
        return res


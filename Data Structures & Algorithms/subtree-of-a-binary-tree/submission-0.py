# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(s, t):
            if not s and not t:
                return True
            elif (s and not t) or (t and not s):
                return False

            if s.val == t.val:
                return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
            return False

        if not root:
            return False
        if isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
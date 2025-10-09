# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = []
        def height(node):
            if node is None:
                return 0
            l_h , r_h = height(node.left) , height(node.right)
            if l_h < 0 or l_h != r_h:
                return -1
            self.ans.append(l_h + 1)
            return l_h + 1
        height(root)
        if k > len(self.ans):
            return -1
        self.ans.sort()
        return (1 << self.ans[-k]) - 1 

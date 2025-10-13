# https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return None , 0       
            left_lca , left_height = dfs(node.left)
            right_lca , right_height = dfs(node.right)
            if left_height > right_height:
                return left_lca , left_height + 1
            elif right_height > left_height:
                return right_lca , right_height + 1
            else:
                return node , left_height + 1
        return dfs(root)[0]

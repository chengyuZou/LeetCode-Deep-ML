class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        @cache
        def dfs(i , j , k):
            if i < 0 or j < 0 or k < 0:
                return -inf
            if i == 0 and j == 0:
                return 0
            
            x = grid[i][j]
            if x > 0:
                k -= 1
            return max(dfs(i - 1 , j , k) , dfs(i , j - 1 , k)) + x
        
        ans = dfs(len(grid) - 1 , len(grid[0]) - 1 , k)
        return -1 if ans < 0 else ans

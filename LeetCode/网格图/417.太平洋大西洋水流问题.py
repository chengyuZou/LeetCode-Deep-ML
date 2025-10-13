class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m , n = len(heights) , len(heights[0])
        def dfs(i: int , j: int , vis: List[List[int]]):
            vis[i][j] = 1
            for x , y in (i + 1 , j) , (i - 1 , j) , (i , j + 1) ,(i , j - 1):
                if 0 <= x < m and 0 <= y < n and not vis[x][y] and heights[x][y] >= heights[i][j]:
                    dfs(x , y , vis)
        vis_P = [[0] * n for _ in range(m)] 
        vis_A = [[0] * n for _ in range(m)]
        for i in range(n):
            dfs(0 , i , vis_P)
            dfs(m - 1 , i , vis_A)
        
        for j in range(m):
            dfs(j , 0 , vis_P)
            dfs(j , n - 1 , vis_A)
        return [[i , j] for i in range(m) for j in range(n) if vis_A[i][j] and vis_P[i][j]]

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10 ** 9 + 7
        m , n = len(grid) , len(grid[0])
        f = [[[0] * k for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][0] = 1
        for i in range(m):
            for j in range(n):
                x = grid[i][j]
                for v in range(k):
                    f[i + 1][j + 1][(v + x) % k] = (f[i][j + 1][v] + f[i + 1][j][v]) % MOD
        return f[-1][-1][0]

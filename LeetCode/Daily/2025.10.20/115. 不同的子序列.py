class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m , n = len(s) , len(t)
        if m < n:
            return 0
        
        f = [[1] + [0] * n for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                f[i + 1][j + 1] = f[i][j + 1]
                if s[i] == t[j]:
                    f[i + 1][j + 1] += f[i][j]
        return f[m][n]

    def numDistinct(self, s: str, t: str) -> int:
      m , n = len(s) , len(t)
      @cache
      def dfs(i , j):
          if j < 0:
              return 1
          if i < 0:
              return 0

          if s[i] == t[j]:
              return dfs(i - 1 , j - 1) + dfs(i - 1 , j)
          return dfs(i - 1 , j)
      return dfs(m - 1 , n - 1)

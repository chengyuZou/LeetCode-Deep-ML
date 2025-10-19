class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1) , len(word2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(1 , n + 1):
            f[0][j] = f[0][j - 1] + 1
        for i in range(1 , m + 1):
            f[i][0] = f[i - 1][0] + 1
        
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    f[i + 1][j + 1] = f[i][j]
                else:
                  #f[i][j] , f[i + 1][j] , f[i][j + 1] 分别为替换，删除，插入
                    f[i + 1][j + 1] = min(f[i][j] , f[i + 1][j] , f[i][j + 1]) + 1
        return f[-1][-1]

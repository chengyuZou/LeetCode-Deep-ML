class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word1) , len(word2)
        @cache
        def dfs(i , j):
            if i < 0 or j < 0:
                return 0
            
            if word1[i] == word2[j]:
                return dfs(i - 1 , j - 1) + 1
            return max(dfs(i - 1 , j) , dfs(i , j - 1))
        
        return m + n - 2 * dfs(m - 1 , n - 1)

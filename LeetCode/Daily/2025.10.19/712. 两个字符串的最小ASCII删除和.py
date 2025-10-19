class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m , n = len(s1) , len(s2)
        @cache
        def dfs(i , j):
            if i < 0 or j < 0:
                return 0
            if s1[i] == s2[j]:
                return dfs(i - 1 , j - 1) + int(ord(s1[i]))
            return max(dfs(i - 1 ,j) , dfs(i , j - 1))
        
        ans_1 = 0
        for i in range(m):
            ans_1 += int(ord(s1[i]))
        for j in range(n):
            ans_1 += int(ord(s2[j]))
        return ans_1 - dfs(m - 1 , n - 1) * 2

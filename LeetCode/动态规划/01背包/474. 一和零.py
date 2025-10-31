class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(i , j , k):
            if i < 0:
                return 0 
            c_1 = strs[i].count('1')
            c_0 = strs[i].count('0')
            res = dfs(i - 1 , j , k)
            if c_0 <= j and  c_1 <= k:
                res =  max(res , dfs(i - 1 , j - c_0 , k - c_1) + 1)
            return res
        
        dfs.cache_clear()
        ans = dfs(len(strs) - 1 , m , n)
        return ans if ans > -inf else 0

# https://leetcode.cn/problems/count-number-of-homogenous-substrings/description/
class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        i , j = 0 , 0
        n = len(s)
        ans = 0
        while i < n:
            while j < n and s[i] == s[j]:
                ans += (j - i + 1) % MOD
                j += 1
            i = j
        return ans % MOD

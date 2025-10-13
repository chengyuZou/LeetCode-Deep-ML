# https://leetcode.cn/problems/count-number-of-ways-to-place-houses/description/

class Solution:
    def countHousePlacements(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        f = [1 , 2] + [0] * (n - 1)
        for i in range(2 , n + 1):
            f[i] = (f[i - 1] + f[i - 2]) % MOD
        return f[n] * f[n] % MOD

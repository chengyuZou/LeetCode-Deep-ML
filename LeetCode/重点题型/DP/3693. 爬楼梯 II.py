# https://leetcode.cn/problems/climbing-stairs-ii/description/
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        f = [0] * (n + 1)
        for i in range(1 ,n + 1):
            f[i] = min(f[j] + (i - j) * (i - j) for j in range(max(i - 3 , 0) , i)) + costs[i - 1]
        return f[n]

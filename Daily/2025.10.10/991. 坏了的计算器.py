# https://leetcode.cn/problems/broken-calculator/description/
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue >= target:
            return startValue - target
        ans = 0
        while target != startValue:
            if target % 2 == 1:
                target += 1
                ans += 1
            elif target % 2 == 0 and target > startValue:
                target //= 2
                ans += 1
            elif target % 2 == 0 and target < startValue:
                return startValue - target + ans
        return ans

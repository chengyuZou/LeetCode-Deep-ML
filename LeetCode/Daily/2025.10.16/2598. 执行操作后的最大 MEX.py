# https://leetcode.cn/problems/smallest-missing-non-negative-integer-after-operations/description/?envType=daily-question&envId=2025-10-16
# 参考https://leetcode.cn/problems/smallest-missing-non-negative-integer-after-operations/solutions/2177789/tong-yu-pythonjavacgo-by-endlesscheng-qoan/?envType=daily-question&envId=2025-10-16
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = defaultdict(int)
        for x in nums:
            x = x % value
            cnt[x] += 1
        mex = 0
        while cnt[mex % value]:
            cnt[mex % value] -= 1
            mex += 1
        return mex

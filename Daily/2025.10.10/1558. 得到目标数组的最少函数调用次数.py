class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        div_max = 0
        for x in nums:
            cnt = 0
            while x:
                if x % 2 == 0:
                    x //= 2
                    cnt += 1
                else:
                    x -= 1
                    ans += 1
            div_max = max(cnt , div_max)
        return div_max + ans

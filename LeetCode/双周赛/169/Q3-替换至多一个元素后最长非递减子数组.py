class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 前后缀分解
        n = len(nums)
        if n == 1:
            return 1
        
        ans = 2
        # 后缀
        suf = [0] * n
        suf[-1] = 1
        for i in range(n - 2 , 0 , -1):
            if nums[i + 1] >= nums[i]:
                suf[i] = suf[i + 1] + 1
                ans = max(ans , suf[i] + 1)
            else:
                suf[i] = 1
        
        # 前缀
        pre = 1
        for i in range(1 , n - 1):
            if nums[i - 1] <= nums[i + 1]:
                ans = max(ans , pre + 1 + suf[i + 1])
            if nums[i - 1] <= nums[i]:
                pre += 1
                ans = max(ans , pre + 1)
            else:
                pre = 1
        return ans

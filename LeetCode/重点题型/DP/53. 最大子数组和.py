class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        for i in range(1 , n):
            f[i] = max(f[i - 1] , 0) + nums[i]
        return max(f)

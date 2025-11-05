class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        MOD = 10 ** 9 + 7
        while k:
            heapreplace(nums , nums[0] + 1)
            k -= 1
        
        ans = 1
        for x in nums:
            ans = ans * x % MOD
        return ans

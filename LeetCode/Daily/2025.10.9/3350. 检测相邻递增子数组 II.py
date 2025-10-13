class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        pre_cnt = 0
        cnt = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] <= nums[i]:
                ans = max(ans , min(cnt , pre_cnt) , cnt // 2)
                pre_cnt = cnt
                
                cnt = 1
            else:
                cnt += 1
        ans = max(ans , min(cnt , pre_cnt) , cnt // 2)
        return ans

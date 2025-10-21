class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1
        
        ans = sum_d = 0
        for x , d in sorted(diff.items()):
            sum_d += d
            ans = max(ans , min(sum_d , cnt[x] + numOperations))
        return ans

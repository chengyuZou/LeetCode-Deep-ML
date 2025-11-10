class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = defaultdict(list)
        ans = inf
        for i in range(n):
            cnt[nums[i]].append(i)
            if len(cnt[nums[i]]) >= 3:
                arr  = cnt[nums[i]]
                ans = min(ans , 2 * (arr[-1] - arr[-3]) , 2 * (arr[2] - arr[0]))
        return ans if ans < inf else -1

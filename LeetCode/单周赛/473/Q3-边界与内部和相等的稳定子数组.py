class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        cnt = defaultdict(int)
        s = capacity[0]
        ans = 0
        for last , x in pairwise(capacity):
            ans += cnt[(x , s)]
            cnt[(last , last + s)] += 1
            s += x
        return ans

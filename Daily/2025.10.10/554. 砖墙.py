# https://leetcode.cn/problems/brick-wall/description/
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = defaultdict(int)
        n = len(wall)
        for row in wall:
            cur = 0
            for i in range(len(row) - 1):
                x = row[i]
                cur += x
                cnt[cur] += 1

        mx = 0
        for k , v in cnt.items():
            mx = max(mx , v)
        return n - mx

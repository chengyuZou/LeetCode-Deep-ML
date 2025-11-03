class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        ans = [0] * n
        g = []
        for i , x in enumerate(obstacles):
            j = bisect_left(g , x + 1)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x

            ans[i] = j + 1
        return ans
            

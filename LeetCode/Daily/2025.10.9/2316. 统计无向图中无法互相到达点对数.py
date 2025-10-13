class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x , y in edges:
            g[x].append(y)
            g[y].append(x)

        vis = [False] * n

        def dfs(x):
            vis[x] = True
            brick = 1
            for y in g[x]:
                if not vis[y]:
                    brick += dfs(y)
            return brick
        ans = 0
        pre_brick = 0
        for i in range(n):
            if not vis[i]:
                brick = dfs(i)
                ans += brick * pre_brick
                pre_brick += brick
        return ans

            

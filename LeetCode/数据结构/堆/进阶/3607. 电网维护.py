class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 序号从1开始,因此为(c + 1)
        g = [[] for _ in range(c + 1)]
        
        for x , y in connections:
            g[x].append(y)
            g[y].append(x)
        
        belong = [-1] * (c + 1)
        # 存放每个对应堆的列表
        heaps = []

        def dfs(x):
            belong[x] = len(heaps)
            h.append(x)
            for y in g[x]:
                if belong[y] < 0:
                    dfs(y)
        
        for i in range(1 , c + 1):
            h = []
            if belong[i] >= 0:
                continue
            dfs(i)
            heapify(h)
            heaps.append(h)

        ans = []
        offline = [False] * (c + 1)
        for op , x in queries:
            if op == 2:
                offline[x] = True
                continue
            if not offline[x]:
                ans.append(x)
                continue
            h = heaps[belong[x]]
            while h and offline[h[0]]:
                heappop(h)
            ans.append(h[0] if h else -1)
        return ans

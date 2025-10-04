class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        visited = [False] * len(graph)
        def dfs(node):
            visited[node] = True 
            nonlocal node_id , size
            size += 1
            if node_id != -2 and node in initial:
                node_id = node if node_id == -1 else -2
            for y , conn in enumerate(graph[node]):
                if not visited[y] and conn:
                    dfs(y)
        
        ans = -1
        max_size = 0
        for x in initial:
            if visited[x]: continue
            node_id = -1
            size = 0
            dfs(x)
            if node_id >= 0 and (size > max_size or (size == max_size and node_id < ans) ):
                ans = node_id
                max_size = size
        return min(initial) if ans < 0 else ans

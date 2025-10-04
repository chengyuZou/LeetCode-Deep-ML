class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        vis = [0] * len(arr)
        def dfs(i):
            if i < 0 or i >= len(arr) or vis[i]:
                return False
            vis[i] = True
            if arr[i] == 0:
                return True
            return dfs(i - arr[i]) or dfs(i + arr[i])
        return dfs(start)

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(profits , capital) , key = lambda x: x[1])

        heap = []
        index = 0
        while k:
            while index < n and projects[index][1] <= w:
                heappush(heap , -projects[index][0])
                index += 1
            
            if heap:
                w -= heappop(heap)
            else:
                break
            k -= 1
        return w

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        heap = [1]
        for _ in range(n):
            x = heappop(heap)
            while heap and x == heap[0]:
                x = heappop(heap)
            a , b , c = x * 2 , x * 3 , x * 5
            for t in [a , b , c]:
                heappush(heap, t)
        return x

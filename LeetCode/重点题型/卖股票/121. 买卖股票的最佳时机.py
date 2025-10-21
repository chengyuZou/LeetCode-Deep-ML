class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for p in prices:
            ans = max(p - min_price , ans)
            min_price = min(p,  min_price)
        return ans
        

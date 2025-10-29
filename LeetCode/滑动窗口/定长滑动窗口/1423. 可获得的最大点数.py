class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 转换为求中间段的min值
        # 求k的最大，即n - k的最小
        ans = inf
        n = len(cardPoints)
        length = n - k
        if not length:
            return sum(cardPoints)
        vocal = 0
        for i , x in enumerate(cardPoints):
            vocal += x

            left = i - length + 1
            if left < 0:
                continue
            
            ans = min(ans , vocal)

            # 左窗口移除
            vocal -= cardPoints[left]

        return sum(cardPoints) - ans

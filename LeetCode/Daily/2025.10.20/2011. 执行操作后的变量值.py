class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for c in operations:
            if "-" in c:
                ans -= 1
            else:
                ans += 1
        return ans

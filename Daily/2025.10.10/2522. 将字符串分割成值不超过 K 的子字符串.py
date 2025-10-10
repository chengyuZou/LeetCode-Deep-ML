# https://leetcode.cn/problems/partition-string-into-substrings-with-values-at-most-k/description/
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 0
        v = 0
        for c in map(int , s):
            if c > k:
                return -1
            v = v * 10 + c
            if v > k:
                ans += 1
                v = c
        
        return ans + 1
            

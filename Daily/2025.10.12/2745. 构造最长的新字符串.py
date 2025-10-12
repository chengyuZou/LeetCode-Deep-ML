# https://leetcode.cn/problems/construct-the-longest-new-string/description/

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        value = 2 * z + min(x , y) * 4
        return value + 2 if x != y else value 

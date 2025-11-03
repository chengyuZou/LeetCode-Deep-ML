class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums=sorted([abs(i) for i in nums])
        return nums[-1]*nums[-2]*100000

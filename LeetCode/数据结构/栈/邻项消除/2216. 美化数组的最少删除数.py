class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack = []
        for x in nums:
            if stack and len(stack) % 2 == 1 and stack[-1] == x:
                stack.pop()

            stack.append(x)
        if len(stack) % 2:
            stack.pop()
        return len(nums) - len(stack)

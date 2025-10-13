class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and self.check(stack[-1] , c):
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

    def check(self ,char1: str , char2: str) -> bool:
        ans = abs(ord(char1) - ord(char2))
        return ans == 1 or ans == 25

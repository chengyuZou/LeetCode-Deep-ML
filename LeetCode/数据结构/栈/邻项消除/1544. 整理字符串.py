class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            #判断
            if stack and stack[-1].lower() == c.lower() and c != stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

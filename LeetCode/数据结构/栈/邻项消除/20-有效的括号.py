class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if stack and self.check(stack[-1] , c):
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0

    def check(self, x , y):
        if x == '(' and y == ")" \
            or x == '[' and y == ']' \
            or x == '{' and y == '}':
            return True
        return False

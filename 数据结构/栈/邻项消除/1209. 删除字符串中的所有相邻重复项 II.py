class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and c == stack[-1][0] and stack[-1][1] == k - 1:
                stack.pop()
            else:
                if stack and c != stack[-1][0] or not stack:
                    stack.append([c , 1])
                else:
                    stack[-1][1] += 1
        return ''.join(c * cnt for c , cnt in stack)

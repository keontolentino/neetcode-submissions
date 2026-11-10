class Solution:
    def isValid(self, s: str) -> bool:
        hMap = {')':'(',
        '}':'{',
        ']':'['}
        stack = []

        for c in s:
            if c in hMap.values():
                stack.append(c)
            else:
                if stack and stack[-1] == hMap[c]:
                    stack.pop()
                else:
                    return False
        return not stack
class Solution:
    def isValid(self, s: str) -> bool:
        dct = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c not in dct:
                stack.append(c)
            else:
                if stack and c in dct and stack[-1] == dct[c]:
                    stack.pop()
                else:
                    return False
        return not stack
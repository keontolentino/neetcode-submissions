class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in mapper:
                if stack and stack[-1] == mapper[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True
        
                
        
            
            
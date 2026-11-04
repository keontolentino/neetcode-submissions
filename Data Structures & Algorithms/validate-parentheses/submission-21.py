class Solution:
    def isValid(self, s: str) -> bool:
        hMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        lst = []

        for c in s:
            if c in hMap.values():
                lst.append(c)
            else:
                if lst and lst[-1] == hMap[c]:
                    lst.pop()
                else:
                    return False

            
        return not lst

class Solution:
    def isValid(self, s: str) -> bool:
        dct = {")": "(",
        "]" : "[",
        "}" : "{"}

        lst = []

        for c in s:
            if c in dct.values():
                lst.append(c)
            else:
                if lst and lst[-1] == dct[c]:
                    lst.pop()
                else:
                    return False
            
        return not lst
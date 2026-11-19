class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        while '()' in s or '{}' in s or '[]' in s:
            if '()' in s:
                s = s.replace('()', '')
            elif '{}' in s:
                s = s.replace('{}', '')
            elif '[]' in s:
                s = s.replace('[]', '')
        return not s 
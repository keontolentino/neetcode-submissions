class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        big = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if big < arr[j]:
                    big = arr[j]
            arr[i] = big
            big = 0
        arr[-1] = -1
        return arr
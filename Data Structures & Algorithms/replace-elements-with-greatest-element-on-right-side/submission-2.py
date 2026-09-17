class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            lst = []
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
            for j in range(i+1, len(arr)):
                lst.append(arr[j])
            arr[i] = max(lst)

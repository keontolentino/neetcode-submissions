class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            cur_max = 0
            if i == len(arr) - 1:
                arr[i] = -1
                return arr
            for j in range(i+1,len(arr)):
                if arr[j] > cur_max:
                    cur_max = arr[j]
            arr[i] = cur_max

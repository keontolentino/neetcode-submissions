class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lst = []
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                if nums[-1] and num == 1:
                    lst.append(count)
            else:
                lst.append(count)
                count = 0
        return max(lst)
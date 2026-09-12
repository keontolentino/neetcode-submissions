class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = []
        count = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                max_count.append(count)
                count = 0
            else:
                count += 1
        max_count.append(count)
        return max(max_count)
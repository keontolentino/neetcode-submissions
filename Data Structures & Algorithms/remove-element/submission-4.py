class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        lst = []
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                lst.append(nums[i])
                k += 1
        for i in range(len(lst)):
            nums[i] = lst[i]

        return k
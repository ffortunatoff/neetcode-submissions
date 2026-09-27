class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]   # overwrite with last valid candidate
            else:
                i += 1
        return n
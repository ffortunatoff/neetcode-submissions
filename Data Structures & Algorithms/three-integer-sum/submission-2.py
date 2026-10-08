class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                lr_sum = nums[left] + nums[right]
                if target == lr_sum:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif target > lr_sum:
                    left += 1
                else:
                    right -= 1
        return res

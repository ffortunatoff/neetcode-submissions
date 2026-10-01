class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res_set = set()
        for val in nums:
            if val in res_set:
                return True
            else:
                res_set.add(val)
        return False
                
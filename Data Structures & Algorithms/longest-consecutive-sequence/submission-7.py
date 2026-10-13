class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)
        res = 1

        for num in hashset:
            if (num-1) not in hashset:
                curr_seq = 1
                print(num)    
                # consider this start of a sequence
                while (num+1) in hashset:
                    curr_seq += 1
                    num += 1
                res = max(res, curr_seq)
        return res
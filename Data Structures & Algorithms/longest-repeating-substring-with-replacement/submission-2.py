class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            curr_len = r - l + 1
            max_freq = max(count.values())
            if curr_len - max_freq <= k:
                res = max(res, curr_len)
            else:
                
                count[s[l]] = count[s[l]] - 1
                l += 1

        return res

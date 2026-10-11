class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        i, j = 0, 1
        max_len = 1
        visited_set = set()
        visited_set.add(s[i])

        while j < len(s):
            
            if s[j] not in visited_set:
                max_len = max(max_len, j - i + 1)
            else:
                while s[j] in visited_set:
                    visited_set.remove(s[i])
                    i += 1
            visited_set.add(s[j])
            j+=1

        return max_len
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_frq_map = Counter(s)
        print(str_frq_map)

        if len(s) != len(t):
            return False

        for char in t:
            print(char)
            if char in str_frq_map and str_frq_map[char] > 0:
                str_frq_map[char] -= 1
            else:
                return False
        return True
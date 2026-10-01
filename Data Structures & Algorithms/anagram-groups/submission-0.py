class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for string in strs:
            sorted_str = "".join(sorted(string))
            my_dict[sorted_str].append(string)
        
        return [val for val in my_dict.values()]
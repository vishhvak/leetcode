class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Method 1 - Use memory
        # s_map = {}
        # t_map = {}
        # for char in s:
        #     s_map.get(char, 0) += 1
        # for char in t:
        #     t_map.get(char, 0) += 1
        # return t_map == s_map
    
        # Method 2 - Sort and Compare
        return sorted(s) == sorted(t)
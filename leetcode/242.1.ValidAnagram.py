from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        for char in t:
            counts[char] -= 1
        for value in counts.values():
            if value != 0:
                return False
        return True
        
# metadata
# relevant-topics array, for loop, defaultdict
# time-complexity O(N) 37.15%
# space-complexity O(N) 73.98%
# language python
# difficulty easy
# date 20240306
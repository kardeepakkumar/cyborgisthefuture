class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ""
        ranks = order
        for i in range(26):
            if chr(ord('a')+i) not in ranks:
                ranks += (chr(ord('a')+i))
        counts = collections.defaultdict(int)
        for char in s:
            counts[char] += 1
        for idx, char in enumerate(ranks):
            result += char*counts[char]
        return result
        
# metadata
# relevant-topics array, dictionary
# time-complexity O(N) 87.77%
# space-complexity O(N) 61.09%
# language python
# difficulty medium
# date 20240311
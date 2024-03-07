class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
        
# metadata
# relevant-topics array, defaultdict, tuple, ord 
# time-complexity O(N) 11.65%
# space-complexity O(N) 8.16%
# language python
# difficulty medium
# date 20240307
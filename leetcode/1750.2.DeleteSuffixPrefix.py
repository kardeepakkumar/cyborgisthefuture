class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while(r > l and s[l] == s[r]):
            char = s[l]
            while(r >= l and s[r] == char):
                r -= 1
            while(r >= l and s[l] == char):
                l += 1
        return r - l + 1
        
# metadata
# relevant-topics array, loops
# time-complexity O(N) 65.40%
# space-complexity O(1) 75.83%.
# language python
# difficulty medium
# date 20240305
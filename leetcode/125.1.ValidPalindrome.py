class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while(r>=l):
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# metadata
# relevant-topics array, for loop, isalnum(), lower()
# time-complexity O(N) 57.17%
# space-complexity O(1) 93.59%
# language python
# difficulty easy
# date 20240308
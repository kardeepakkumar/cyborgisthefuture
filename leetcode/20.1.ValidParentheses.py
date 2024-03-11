class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openClose = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in "([{":
                stack.append(openClose[char])
            else:
                if len(stack) == 0 or stack.pop() != char:
                    return False
        return len(stack) == 0
        
# metadata
# relevant-topics stack
# time-complexity O(N) 97.64%
# space-complexity O(1) 79.40%
# language python
# difficulty easy
# date 20240311
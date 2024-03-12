class Solution:
    def isvalid(self, item) -> bool:
        stack = 0
        for char in item:
            if char == '(':
                stack += 1
            else:
                stack -= 1
            if stack < 0:
                return False
        return stack == 0
    def generateParenthesis(self, n: int) -> List[str]:
        result = [""]
        for i in range(0, 2*n):
            result1 = [item + "(" for item in result]
            result2 = [item + ")" for item in result]
            result = result1 + result2
        final = []
        for item in result:
            if self.isvalid(item):
                final.append(item)
        return final
        
# metadata
# relevant-topics exponential
# time-complexity O(2^N) 5.12%
# space-complexity O(2^N) 5.13%
# language python
# difficulty medium
# date 20240312
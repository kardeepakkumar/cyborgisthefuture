class Solution:
    def validate(self, strings, n) -> List[str]:
        result = []
        for string in strings:
            stack = string.count('(') - string.count(')')
            if (len(string) != 2*n and stack >=0) or stack == 0:
                result.append(string)
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        result = [""]
        for i in range(0, 2*n):
            result1 = [item + "(" for item in result]
            result2 = [item + ")" for item in result]
            result = result1 + result2
            result = self.validate(result, n)
        return result
        
# metadata
# relevant-topics exponential
# time-complexity O(2^N) 14.97%
# space-complexity O(2^N) 5.13%
# language python
# difficulty medium
# date 20240312
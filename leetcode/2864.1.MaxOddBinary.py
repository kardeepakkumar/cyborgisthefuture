class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for char in s:
            if char == "1":
                count += 1
        result = "1"*(count-1)
        result = result + "0"*(len(s)-count)
        result = result + "1"
        return result

# metadata
# relevant-topics string, for loop
# time-complexity O(N) 93.00%
# space-complexity O(1) 45.47%
# language python
# difficulty easy
# date 20240301
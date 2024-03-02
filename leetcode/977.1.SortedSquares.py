class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result1, result2 = [], []
        for i, num in enumerate(nums):
            if num < 0:
                result1 = [num*num] + result1
            else:
                result2 = result2 + [num*num]
        result = []
        while(len(result1) > 0 and len(result2) > 0):
            if(result1[0] > result2[0]):
                result.append(result2.pop(0))
            else:
                result.append(result1.pop(0))
        return result + result1 + result2

# metadata
# relevant-topics array, for loop
# time-complexity O(N) 5.04%
# space-complexity O(N) 55.74%
# language python
# difficulty easy
# date 20240302
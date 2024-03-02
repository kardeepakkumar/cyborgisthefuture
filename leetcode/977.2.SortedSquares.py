class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [num*num for num in nums]
        l, r = 0, len(nums)-1
        result = []
        while(l<=r):
            if(squared[l] > squared[r]):
                result = [squared[l]] + result
                l += 1
            else:
                result = [squared[r]] + result
                r -= 1
        return result
# metadata
# relevant-topics array, for loop
# time-complexity O(N) 5.04%
# space-complexity O(N) 72.31%
# language python
# difficulty easy
# date 20240302
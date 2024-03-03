class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        result = 0
        for num in nums:
            if num < k:
                result += 1
        return result
        
# metadata
# relevant-topics array, for loop 
# time-complexity O(N) 100.00%
# space-complexity O(1) 100.00%
# language python
# difficulty easy
# date 20240302

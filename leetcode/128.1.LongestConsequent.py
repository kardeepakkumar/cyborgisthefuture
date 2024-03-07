class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        result = 0
        for n in numsSet:
            if n-1 not in numsSet:
                length = 1
                while n+length in numsSet:
                    length += 1
                result = max(length, result)
        return result
        
# metadata
# relevant-topics array, for loop, set
# time-complexity O(N) 72.91%
# space-complexity O(N) 82.79%
# language python
# difficulty medium
# date 20240307
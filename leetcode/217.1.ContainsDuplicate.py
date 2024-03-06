class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniques = set()
        for num in nums:
            if num in uniques:
                return True
            uniques.add(num)
        return False
        
# metadata
# relevant-topics array, for loop, set 
# time-complexity O(N) 85.65%
# space-complexity O(N) 46.21%
# language python
# difficulty easy
# date 20240306
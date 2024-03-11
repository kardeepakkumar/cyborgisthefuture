class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result1 = set(nums1)
        result2 = set(nums2)
        return list(result1.intersection(result2))
        
# metadata
# relevant-topics set, list 
# time-complexity O(N) 42.97%
# space-complexity O(N) 52.43%
# language python
# difficulty easy
# date 20240310
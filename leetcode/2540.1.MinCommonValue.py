class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0
        while(p1 < len(nums1) and p2 < len(nums2)):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return -1
        
# metadata
# relevant-topics array, for loop 
# time-complexity O(N) 89.74%
# space-complexity O(1) 73.75%
# language python
# difficulty easy
# date 20240309
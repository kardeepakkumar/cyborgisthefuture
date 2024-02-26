class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if(nums[i] + nums[j] == target):
                    return([i,j])

# metadata
# relevant-topics array, for loop 
# time-complexity O(N^2) 17.72%
# space-complexity O(1) 80.82%
# language python
# difficulty easy
# date 20240222
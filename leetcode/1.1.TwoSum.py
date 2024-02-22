class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if(nums[i] + nums[j] == target):
                    return([i,j])

# Key Concepts: array, for loop 
# Time Complexity: O(N^2): 17.72%
# Space Complexity: O(1): 80.82%
                
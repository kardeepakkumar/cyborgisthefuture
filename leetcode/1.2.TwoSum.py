class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if(complement in num_map):
                return([num_map[complement], i])
            else:
                num_map[num] = i
# Key Concepts: hash table/dictionary, enumerate, for loop
# Time Complexity: O(N): 87.78%
# Space Complexity: O(N): 75.94%
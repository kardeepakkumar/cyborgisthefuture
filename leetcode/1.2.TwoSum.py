class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if(complement in num_map):
                return([num_map[complement], i])
            else:
                num_map[num] = i

# metadata
# relevant-topics hash table/dictionary, enumerate, for loop
# time-complexity O(N) 87.78%
# space-complexity O(N) 75.94%
# language python
# difficulty easy
# date 20240222
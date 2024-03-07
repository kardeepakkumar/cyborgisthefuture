class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            result[i] = result[i-1]*nums[i-1]
        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            postfix *= nums[i+1]
            result[i] *= postfix
        return result
        
# metadata
# relevant-topics array, for loop 
# time-complexity O(N) 56.09%
# space-complexity O(1) 96.21%
# language python
# difficulty medium
# date 20240307
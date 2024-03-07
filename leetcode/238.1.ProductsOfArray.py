class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for i in range(len(nums))]
        right = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
            right[len(nums)-i-1] = right[len(nums)-i]*nums[len(nums)-i]
        result = []
        for i in range(0, len(nums)):
            result.append(left[i]*right[i])
        return result
        
# metadata
# relevant-topics array, for loop
# time-complexity O(N) 6.77%
# space-complexity O(N) 21.89%
# language python
# difficulty medium
# date 20240307
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        i = 0
        while(i < len(nums)-2):
            l, r = i+1, len(nums)-1
            while(r > l):
                cur = nums[l] + nums[r]
                if cur == -nums[i]:
                    result.append([nums[i], nums[l], nums[r]])
                    nl = nums[l]
                    while(l<r and nums[l] == nl):
                        l += 1
                    nr = nums[r]
                    while(l<r and nums[r] == nr):
                        r -= 1
                elif cur > -nums[i]:
                    r -= 1
                else:
                    l += 1
            n = nums[i]
            while(i < len(nums)-2 and nums[i] == n):
                i += 1
            if nums[i] > 0:
                break
        return result
        
# metadata
# relevant-topics array, while loop, 2 pointers
# time-complexity O(N^2) 74.68% 
# space-complexity O(logN) 76.41%
# language python
# difficulty medium
# date 20240307
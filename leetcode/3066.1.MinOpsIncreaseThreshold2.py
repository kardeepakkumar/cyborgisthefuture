class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        def binarySearchIndex(start, end, val):
            while start<= end:
                mid = (start + end)//2
                if nums[mid] == val:
                    return mid
                elif nums[mid] < val:
                    start = mid + 1
                else:
                    end = mid-1
            return start
        result = 0   
        while(nums[0] < k):
            x = nums.pop(0)
            y = nums.pop(0)
            idx = binarySearchIndex(0, len(nums)-1, 2*x + y)
            nums.insert(idx, 2*x + y)
            result += 1
        return result
        
# metadata
# relevant-topics array, for loop, binary search 
# time-complexity O(NlogN) 100.00%
# space-complexity O(N) 100.00%
# language python
# difficulty medium
# date 20240302

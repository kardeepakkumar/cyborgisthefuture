class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        cur = numbers[l] + numbers[r]
        while(cur != target):
            if(cur > target):
                r -= 1
            else:
                l += 1
            cur = numbers[l] + numbers[r]
        return ([l+1, r+1])
        
# metadata
# relevant-topics array, while loop, 2 pointers
# time-complexity O(N) 32.75%
# space-complexity O(1) 41.10%
# language python
# difficulty medium
# date 20240307
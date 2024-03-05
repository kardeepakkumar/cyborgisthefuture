class Solution:
    def binSearch(self, changeIndices, nums):
        last_indices = {}
        for i, idx in enumerate(changeIndices):
            last_indices[idx] = i
        if(len(last_indices.keys()) != len(nums)):
            return False
        count = 0
        for i, idx in enumerate(changeIndices):
            if(last_indices[idx] == i):
                if(count >= nums[idx-1]):
                    count -= nums[idx-1]
                else:
                    return False
            else:
                count += 1
        return True
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        l, r = 0, len(changeIndices) - 1
        while(r >= l):
            m = (l+r)//2
            if self.binSearch(changeIndices[:m+1], nums):
                r = m - 1
            else:
                l = m + 1
        if(l > len(changeIndices) - 1):
            return -1
        else:
            return l + 1
            
# metadata
# relevant-topics binary search
# time-complexity O(NlogN) 50.64%
# space-complexity O(N) 71.28%
# language python
# difficulty medium
# date 20240305
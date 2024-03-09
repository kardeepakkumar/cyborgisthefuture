class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        l, r = 0, len(height) - 1
        while(r>l):
            vol = (r-l)*min(height[l], height[r])
            maxVol = max(vol, maxVol)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxVol
        
# metadata
# relevant-topics array, for loop, 2 pointers
# time-complexity O(N) 8.56%
# space-complexity O(1) 36.68%
# language python
# difficulty medium
# date 20240308
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l,r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                result += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                result += rightMax - height[r]
        return result
        
# metadata
# relevant-topics array, 2 pointers
# time-complexity O(N) 73.36%
# space-complexity O(1) 77.72%
# language python
# difficulty hard
# date 20240311
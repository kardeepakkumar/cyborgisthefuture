class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
        max_count = max(counts.values())
        result = 0
        for v in counts.values():
            if v == max_count:
                result += v
        return result
        
# metadata
# relevant-topics array, for loop, defaultdict
# time-complexity O(N) 87.93%
# space-complexity O(N) 97.35%
# language python
# difficulty easy
# date 20240308
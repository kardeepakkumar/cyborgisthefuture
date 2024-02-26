from collections import Counter
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        num_most_common = Counter(nums).most_common(1)[0][1]
        if(num_most_common > 2):
            return False
        else:
            return True
        
# metadata
# relevant-topics counter, Counter().most_common
# time-complexity O(N) 100.00%
# space-complexity O(N) 100.00%
# language python
# difficulty easy
# date 20240225
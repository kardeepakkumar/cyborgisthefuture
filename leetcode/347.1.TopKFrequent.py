class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
        min_count = sorted(counts.values(), reverse=True)[k-1]
        result = []
        for key in counts.keys():
            if counts[key] >= min_count:
                result.append(key)
        return result
        
# metadata
# relevant-topics array, for loop, dictionary 
# time-complexity O(NlogN) 21.80%
# space-complexity O(N) 91.81%
# language python
# difficulty medium
# date 20240307
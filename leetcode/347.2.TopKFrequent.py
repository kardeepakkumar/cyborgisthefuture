class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.defaultdict(int)
        for num in nums:
            counts[num] += 1
        freqs = [[] for i in range(0, len(nums)+1)]
        for num, freq in counts.items():
            freqs[freq].append(num)
        result = []
        f = len(nums)
        while(len(result) < k):
            result += freqs[f]
            f -= 1
        return result

# metadata
# relevant-topics array, for loop, dictionary
# time-complexity O(N) 34.14%
# space-complexity O(N) 20.19%
# language python
# difficulty medium
# date 20240307
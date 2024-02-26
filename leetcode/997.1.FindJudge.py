class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_counts = dict.fromkeys(range(1, n+1), 0)
        not_judge = set()
        for t in trust:
            not_judge.add(t[0])
            trust_counts[t[1]] += 1
        for key in trust_counts:
            if(trust_counts[key] == n-1 and key not in not_judge):
                return key
        return -1
    
# metadata
# relevant-topics for loop, set, dict.fromkeys
# time-complexity O(T+N) 93.11%
# space-complexity O(N) 86.28%
# language python
# difficulty easy
# date 20240222
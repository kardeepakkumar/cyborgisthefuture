class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0]*n
        stack = [] # temp, idx
        for i, T in enumerate(temperatures):
            while stack and stack[-1][0] < T:
                t, idx = stack.pop()
                answer[idx] = i - idx
            stack.append([T, i])
        return answer
        
# metadata
# relevant-topics stack
# time-complexity O(N) 85.39%
# space-complexity O(N) 10.46%
# language python
# difficulty medium
# date 20240312
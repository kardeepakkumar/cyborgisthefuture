class Solution:
    def findJudge(self, N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

# Key Concepts: for loop
# Time Complexity: O(T+N): 88.42%
# Space Complexity: O(N): 66.79%
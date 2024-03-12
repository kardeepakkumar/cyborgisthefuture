class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[""], ["()"]]
        for i in range(2, n+1):
            dp.append([])
            for j in range(0, i):
                for inside in dp[j]:
                    dp[i] += ["(" + inside + ")" + outside for outside in dp[i-j-1]]
        return dp[n]
        
# metadata
# relevant-topics dynamic programming
# time-complexity O(2^N) 51.35%
# space-complexity O(2^N) 50.95%
# language python
# difficulty medium
# date 20240312
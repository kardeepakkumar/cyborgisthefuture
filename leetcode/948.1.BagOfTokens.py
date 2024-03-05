class Solution:
    def increase(self):
        while len(self.tokens) > 0 and self.tokens[0] <= self.power:
            self.power -= self.tokens[0]
            self.score += 1
            self.tokens.pop(0)
        self.decrease()
    def decrease(self):
        if (len(self.tokens) > 1 and self.score > 0):
            self.score -= 1
            self.power += self.tokens[-1]
            self.tokens.pop(-1)
            self.increase()
        
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
    	self.score = 0
        self.tokens = sorted(tokens)
        self.power = power
        self.increase()
        return self.score
        
# metadata
# relevant-topics recursion, while loop
# time-complexity O(NlogN) 64.44%
# space-complexity O(N) 94.14%
# language python
# difficulty medium
# date 20240304
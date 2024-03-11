class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops ="+-*/"
        for t in tokens:
            if t in ops:
                d2 = int(stack.pop())
                d1 = int(stack.pop())
                if t == '*':
                    result = d1*d2
                elif t == '/':
                    result = d1/d2
                elif t == '+':
                    result = d1 + d2
                else:
                    result = d1 - d2
                stack.append(int(result))
            else:
                stack.append(t)
        return int(stack[-1])
        
# metadata
# relevant-topics stack
# time-complexity O(N) 49.89%
# space-complexity O(N) 37.55%
# language python
# difficulty medium
# date 20240311
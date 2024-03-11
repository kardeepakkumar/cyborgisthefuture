class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(len(self.min) == 0 or val <= self.min[-1]):
            self.min.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# metadata
# relevant-topics stack
# time-complexity O(1) 74.65%
# space-complexity O(N) 82.04%
# language python
# difficulty medium
# date 20240311
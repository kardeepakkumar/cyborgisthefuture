class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pos = sorted(list(zip(position, speed)), key=lambda x: x[0])
        time = [(target-sorted_pos[i][0])/sorted_pos[i][1] for i in range(0, len(speed))]
        stack = []
        for t in time:
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)
        
# metadata
# relevant-topics array, for loop 
# time-complexity O(NlogN) 73.11%
# space-complexity O(N) 17.26%
# language python
# difficulty medium
# date 20240312
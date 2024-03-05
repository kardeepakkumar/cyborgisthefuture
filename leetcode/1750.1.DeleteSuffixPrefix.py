class Solution:
    def minimumLength(self, s: str) -> int:
        word = [char for char in s]
        while(len(word) > 1):
            if(word[0] != word[-1]):
                break
            char = word[0]
            while(len(word) > 0 and word[-1] == char):
                word.pop(-1)
            while(len(word) > 0 and word[0] == char):
                word.pop(0)
        return len(word)
        
# metadata
# relevant-topics array, loops
# time-complexity O(N) 5.21%
# space-complexity O(N) 5.21%
# language python
# difficulty medium
# date 20240305
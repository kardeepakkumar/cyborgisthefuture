class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while(i < len(s)):
            w_size = ""
            while(s[i] != '#'):
                w_size += s[i]
                i += 1
            result.append(s[i+1:i+1+int(w_size)])
            i += int(w_size) + 1
        return result
        
# metadata
# relevant-topics array, for loop 
# time-complexity O(N) 100.00%
# space-complexity O(N) 100.00%
# language python
# difficulty medium
# date 20240307
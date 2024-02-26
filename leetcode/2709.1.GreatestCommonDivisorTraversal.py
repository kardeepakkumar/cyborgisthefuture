class UnionFind:
    def __init__(self, count):
        self.count = count
        self.size = [1]*self.count
        self.par = [i for i in range(self.count)]

    def find(self, x):
        if(self.par[x] != x):
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if(p1 == p2):
            return
        if(self.size[p1] > self.size[p2]):
            self.par[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.par[p1] = p2
            self.size[p2] += self.size[p1]
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        f_idx = {}
        for i, n in enumerate(nums):
            f = 2
            while f*f <= n:
                if(n % f == 0):
                    if(f in f_idx.keys()):
                        uf.union(f_idx[f], i)
                    else:
                        f_idx[f] = i
                while(n%f == 0):
                    n //= f
                f += 1
            if (n > 1):
                if(n in f_idx.keys()):
                    uf.union(f_idx[n], i)
                else:
                    f_idx[n] = i
        return uf.count == 1
    
# metadata
# relevant-topics union find, prime numbers
# time-complexity O(N*SQRT(MAX(NUMS))) 31.25%
# space-complexity O(N) 93.75%
# language python
# difficulty hard
# date 20240225
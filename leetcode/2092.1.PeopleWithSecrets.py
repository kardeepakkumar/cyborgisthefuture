class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        result = {0, firstPerson}

        time_map = {}
        for src, dst, t in meetings:
            if(t not in time_map.keys()):
                time_map[t] = defaultdict(list)
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)

        def dfs(src, adj):
            if src in visited:
                return
            result.add(src)
            visited.add(src)
            for node in adj[src]:
                dfs(node, adj)

        for t in sorted(time_map.keys()):
            visited = set()
            for src in time_map[t].keys():
                if src in result:
                    dfs(src, time_map[t])

        return (list(result))
    
# metadata
# relevant-topics dfs, defaultdict, adjacency graph
# time-complexity O(MlogM) 82.78%
# space-complexity O(M) 11.92%
# language python
# difficulty hard
# date 20240224
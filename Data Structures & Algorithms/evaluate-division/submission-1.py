from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)

        for eq, val in zip(equations, values):
            a,b = eq
            adj[a].append((b, val))
            adj[b].append((a, 1/val))

        seen = set()

        def traversal(src, target):
            if src not in adj:
                return -1

            if src == target:
                return 1
            
            if src in seen:
                return -1
            
            seen.add(src)

            for nei in adj[src]:
                if nei in seen:
                    continue
                res = traversal(nei[0], target)

                if res != -1:
                    seen.remove(src)
                    return nei[1] * res

            seen.remove(src)
            return -1

        return [traversal(src, target) for src, target in queries]
            


            

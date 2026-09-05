class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(numCourses)]
        seen = [set() for i in range(numCourses)]

        for src, dst in prerequisites:
            adj[src].append(dst)
        
        def dfs(node):
            if node in seen[node]:
                return seen[node]

            curr_seen = set()
            curr_seen.add(node)

            for nei in adj[node]:
                curr_seen |= dfs(nei)

            seen[node] |= curr_seen
            return curr_seen

        for i in range(numCourses):
            dfs(i)
        
        res = []
        for src, dst in queries:
            ans = True
            if dst not in seen[src]:
                ans = False
            res.append(ans)
        
        return res
             

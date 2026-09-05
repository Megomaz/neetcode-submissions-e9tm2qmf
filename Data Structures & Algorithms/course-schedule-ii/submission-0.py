class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        res = []

        for n1,n2 in prerequisites:
            indegree[n2] += 1
            adj[n1].append(n2)

        q = deque()

        for node, val in enumerate(indegree):
            if val == 0:
                q.append(node)

        while q:
            node = q.popleft()
            res.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return [] if len(res) != numCourses else res[::-1]
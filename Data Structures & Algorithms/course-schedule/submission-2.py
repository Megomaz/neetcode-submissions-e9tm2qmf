class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for src,dst in prerequisites:
            adj_list[src].append(dst)
            indegree[dst] += 1
        
        q = deque()

        for idx,val in enumerate(indegree):
            if val != 0:
                continue
            q.append(idx)
        
        seen = 0

        while q:
            node = q.popleft()
            seen += 1

            for nei in adj_list[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return seen == numCourses
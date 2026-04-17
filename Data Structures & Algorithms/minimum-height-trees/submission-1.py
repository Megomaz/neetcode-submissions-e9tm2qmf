class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        ans = [0]
        nodes = defaultdict(list)
        
        for u,v in edges:
            nodes[u].append(v)
            nodes[v].append(u)

        q = deque()
        edges_cnt = [0] * n
        for i in range(n):
            if len(nodes[i]) <= 1:
                q.append(i)
            edges_cnt[i] = len(nodes[i])

        while q:
            if n <= 2:
                return list(q)

            size = len(q)
            
            for _ in range(size):
                node = q.popleft()

                n -=1
                for nei in nodes[node]:
                    edges_cnt[nei] -= 1
                    if edges_cnt[nei] == 1:
                        q.append(nei)

        return ans
        

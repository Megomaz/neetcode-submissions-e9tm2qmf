class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        parent = [idx for idx in range(len(points))]
        rank = [1 for _ in range(len(points))]
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return parent[node]

        def union(p1,p2):
            root1,root2 = find(p1),find(p2)

            if root1 == root2:
                return False
            
            if rank[root1] > rank[root2]:
                rank[root1] += rank[root2]
                parent[root2] = root1
            else:
                rank[root2] += rank[root1]
                parent[root1] = root2
            return True
        
        edges = []

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                weight = abs(x1 - x2) + abs(y2 - y1)
                edges.append((i,j,weight))

        edges.sort(key=lambda x:x[2])

        for u,v,w in edges:
            if union(u,v):
                res += w

        return res


            


            

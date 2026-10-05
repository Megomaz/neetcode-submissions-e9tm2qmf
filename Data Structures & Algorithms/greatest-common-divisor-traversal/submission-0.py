import math
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        parent = [i for i in range(len(nums))]
        size = [1] * len(nums)
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2:
                return
            
            if size[p1] < size[p2]:
                parent[p1] = p2
                size[p2] += size[p1]
            else:
                parent[p2] = p1
                size[p1] += size[p2]
            return
            
        for i in range(len(nums)):
            for j in range(len(nums)):
                if math.gcd(nums[i], nums[j]) != 1:
                    union(i,j)
        val = find(0)

        for i in range(1,len(nums)):
            if find(i) != val:
                return False
        return True
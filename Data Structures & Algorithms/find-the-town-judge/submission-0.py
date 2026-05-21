class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # town judge trusts no one -> 1 - ..., 2-1, 3-1,

        # 1,2,3,4
        # trusts = [2,1,0,3]
        # trusted_by = [2,0,3,1]

        trusts = [0] * n
        trusted_by = [0] * n

        for t,trust_by in trust:
            trusts[t - 1] += 1
            trusted_by[trust_by - 1] += 1
        
        for i in range(n):
            if trusts[i] == 0 and trusted_by[i] == n-1:
                return i + 1
        return -1
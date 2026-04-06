class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def dfs(i,arr):
            if len(arr) == k:
                combinations.append(arr[:])
                return

            if i > n:
                return

            # 2 options:
            arr.append(i)
            dfs(i+1, arr)
            arr.pop()

            dfs(i+1, arr)


        dfs(1,[])
        return combinations
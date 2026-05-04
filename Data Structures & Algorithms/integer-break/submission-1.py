class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {1:1}

        def dfs(num):
            # base case
            if num in cache:
                return cache[num]

            val = 0

            for i in range(1,num):
                val = max(
                    val, max(i, dfs(i)) * max(num - i, dfs(num - i))
                )

            cache[num] = val
            return val

        return dfs(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(back,front,cur):
            if back == n and front == n:
                word = ''.join(cur)
                res.append(word)
                return 

            if back < n:
                cur.append('(')
                backtrack(back + 1, front,cur)
                cur.pop()

            if back >= front + 1:
                cur.append(')')
                backtrack(back, front + 1,cur)
                cur.pop()

        backtrack(0,0,[])
        return res

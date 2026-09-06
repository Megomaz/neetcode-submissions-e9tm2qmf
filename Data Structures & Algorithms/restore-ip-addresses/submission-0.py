class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []

        def backtrack(i, curr, res):
            if i == len(s):
                if len(res) == 4 and curr == '':
                    answer.append('.'.join(res))
                return

            curr += s[i]

            if len(curr) > 3 or int(curr) > 255 or (curr[0] == '0' and len(curr) > 1):
                return
                    

            #add a dot
            if len(res) < 4:
                res.append(curr)
                backtrack(i+1, '', res)
                res.pop()

            # skip placing a dot
            backtrack(i+1, curr, res)

        backtrack(0,'',[])
        return answer
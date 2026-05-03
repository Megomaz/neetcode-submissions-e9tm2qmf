class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1 = 0
        n = len(s)
        for r in range(len(t)):
            if l1 == n:
                return True

            if s[l1] == t[r]:
                l1 += 1

        return l1 == n
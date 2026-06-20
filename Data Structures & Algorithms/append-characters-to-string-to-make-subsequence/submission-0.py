class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = l1 = 0

        while l < len(s) and l1 < len(t):
            if s[l] == t[l1]:
                l1 += 1
            
            l += 1

        return len(t) - l1
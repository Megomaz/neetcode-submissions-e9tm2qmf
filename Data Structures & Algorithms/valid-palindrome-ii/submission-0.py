class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isPalindrome(l,r):

            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1

            return True

        while l < r:
            if s[l] != s[r]:
                if isPalindrome(l+1,r) or isPalindrome(l,r - 1):
                    return True
                else:
                    return False
            l +=1
            r -=1
        return True
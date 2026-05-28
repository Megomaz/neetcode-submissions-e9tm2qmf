class Solution:
    def minWindow(self, s: str, t: str) -> str:
        size_s,size_t = len(s),len(t)
        if size_t > size_s:

            return ""

        # count letters in t
        # count letters in curr window in s
        # if fine, increment left pointer
        have,need = {},Counter(t)
        l = 0
        ans,string = float('inf'), None

        for r in range(size_s):
            have[s[r]] = have.get(s[r],0) + 1

            while all(have.get(k, 0) >= v for k, v in need.items()):
                if r - l + 1 < ans:
                    ans = r - l + 1
                    string = (l,r)
                have[s[l]] -= 1
                ans = min(ans, r - l + 1)
                l += 1
        return "" if ans == float('inf') else s[string[0]:string[1]+1]


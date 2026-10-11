class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for word in strs:
            w = sorted(word)
            w = ''.join(w)
            seen[w].append(word)
        
        return list(seen.values())
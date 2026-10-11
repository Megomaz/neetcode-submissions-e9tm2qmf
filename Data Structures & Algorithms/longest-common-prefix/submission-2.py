class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()

        def insert(word):
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.isWord = True
        
        for word in strs:
            insert(word)
        
        res = ''
        strs.sort(key=lambda x:len(x))
        for char in strs[0]:
            if len(root.children) > 1:
                return res
            res += char
            root = root.children[char]
        return res
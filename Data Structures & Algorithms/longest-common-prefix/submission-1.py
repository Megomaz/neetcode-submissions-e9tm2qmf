class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        prefix = []
        

        def insert(word):
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            curr.isEndOfWord = True

        for word in strs:
            insert(word)
        
        curr = root
        while curr.children and len(curr.children) == 1 and not curr.isEndOfWord:
            key = curr.children.keys()
            for char in key:
                prefix.append(char)
                
                curr = curr.children[char]
        return ''.join(prefix)
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isEndofWord = False

    def insert(self,word):
        root = self

        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()

            root = root.children[char]
        root.isEndofWord = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()
        root = TrieNode()
        visiting = set()
        rows,cols = len(board), len(board[0])

        for word in words:
            root.insert(word)

        def dfs(row,col,node,curr_word):
            if not 0 <= row < rows or not 0 <= col < cols or (row,col) in visiting or board[row][col] not in node.children:
                return 
            
            node = node.children[board[row][col]]
            curr_word += board[row][col]
            if node.isEndofWord:
                res.add(curr_word)   
            visiting.add((row,col))

            dfs(row + 1, col, node,curr_word) 
            dfs(row - 1, col, node,curr_word) 
            dfs(row, col + 1, node,curr_word)
            dfs(row, col - 1, node,curr_word)

            visiting.remove((row,col))
            

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(res)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        used = set()

        def cycleLetters(i):
            return chr(ord('a') + i )

        q = deque()
        q.append(beginWord)
        count = 1

        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()

                if word == endWord and endWord in wordList:
                    return count

                used.add(word)
                print(used)
                for i in range(len(word)):
                    for j in range(26):
                        new_word = word[:i] + cycleLetters(j)+ word[i+1:]
                        
                        if new_word in wordList and new_word not in used:
                            q.append(new_word)
                            print(new_word)
            count +=1    
                        
           
        return 0 

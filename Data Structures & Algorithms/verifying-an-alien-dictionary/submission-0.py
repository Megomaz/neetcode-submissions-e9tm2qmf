class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordered = {char:i for i,char in enumerate(order)}

        for i in range(1,len(words)):
            word1,word2 = words[i-1], words[i]
        
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                
                if ordered[word1[j]] > ordered[word2[j]]:
                    return False
                elif ordered[word1[j]] < ordered[word2[j]]:
                    break
        return True
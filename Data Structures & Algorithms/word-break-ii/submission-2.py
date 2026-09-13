class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}

        def backtrack(i):
            if i == len(s):
                return ['']

            if i in dp:
                return dp[i]
            
            all_sentences = []

            for word in wordDict:
                if len(word) + i > len(s) or s[i: i + len(word)] != word:
                    continue
                
                
                remaining_sentences = backtrack(i+len(word))
                
                for sentences in remaining_sentences:
                    if sentences: # or sentences != ['']
                        all_sentences.append(word + ' ' + sentences)
                    else: # i == len(s)
                        all_sentences.append(word)
            
            dp[i] = all_sentences
            return all_sentences

        return backtrack(0)
                
               
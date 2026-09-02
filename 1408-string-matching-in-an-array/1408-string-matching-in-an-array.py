class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        full_text = " ".join(words)
    
        for word in words:
            if full_text.count(word) > 1:
                result.append(word)
            
        return result
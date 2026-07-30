class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Teeno rows ke sets banaye
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        res = []
        
        for w in words:
            # Case-insensitivity ke liye lowercase kiya
            w_lower = set(w.lower())
            
            # Subset check: kya saare characters ek hi row me hain?
            if w_lower <= row1 or w_lower <= row2 or w_lower <= row3:
                res.append(w)
                
        return res
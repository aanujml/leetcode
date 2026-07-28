class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        
        # String par index ke saath loop chalao
        for i, char in enumerate(s):
            # Pehla aisa character jiski frequency 1 ho
            if count[char] == 1:
                return i
                
        return -1
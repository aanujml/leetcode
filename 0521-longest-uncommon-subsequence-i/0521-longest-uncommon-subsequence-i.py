class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        
        # Step 2: Agar different hain, toh longer string hi answer hai
        return max(len(a), len(b))
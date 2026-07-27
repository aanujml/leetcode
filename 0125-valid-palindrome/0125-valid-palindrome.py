class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [char.lower() for char in s if char.isalnum()]
        
        # Original filtered list ko uske reverse se compare karein
        return filtered == filtered[::-1]
        

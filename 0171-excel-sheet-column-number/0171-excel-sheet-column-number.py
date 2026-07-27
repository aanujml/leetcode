class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            # Current digit ka value: 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
            value = ord(char) - ord('A') + 1
            ans = ans * 26 + value
            
        return ans
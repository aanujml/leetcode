class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # s + s banaya, pehle aur aakhri char ko drop karke check kiya
        return s in (s + s)[1:-1]
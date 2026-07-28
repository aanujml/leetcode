class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # Pattern aur words ki count same honi chahiye
        if len(pattern) != len(words):
            return False
            
        # One-liner set condition for bijection (Isomorphic logic)
        return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))
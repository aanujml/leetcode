class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_to_t = {}
        map_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check 1: Agar char_s pehle se mapped hai, toh same char_t hona chahiye
            if char_s in map_s_to_t and map_s_to_t[char_s] != char_t:
                return False
                
            # Check 2: Agar char_t pehle se mapped hai, toh same char_s hona chahiye
            if char_t in map_t_to_s and map_t_to_s[char_t] != char_s:
                return False
                
            # Mapping establish karo
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s
            
        return True
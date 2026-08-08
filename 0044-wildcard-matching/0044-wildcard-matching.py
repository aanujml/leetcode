class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = 0
        p_ptr = 0
        star_idx = -1
        s_match = -1
        
        len_s, len_p = len(s), len(p)
        
        while s_ptr < len_s:
            # Case 1: Exact match or '?' match
            if p_ptr < len_p and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            # Case 2: '*' match found in pattern
            elif p_ptr < len_p and p[p_ptr] == '*':
                star_idx = p_ptr
                s_match = s_ptr
                p_ptr += 1
            # Case 3: Mismatch, but we have a previous '*' to backtrack
            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_match += 1
                s_ptr = s_match
            # Case 4: Mismatch and no '*' available
            else:
                return False
                
        # Skip remaining '*' in pattern
        while p_ptr < len_p and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len_p
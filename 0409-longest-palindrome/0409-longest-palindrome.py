class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        has_odd = False
        
        for freq in count.values():
            # Agar frequency even hai, toh poora count le lo
            # Agar odd hai, toh (freq - 1) le lo (even part)
            ans += (freq // 2) * 2
            
            # Agar frequency odd mili, toh flag True kar do
            if freq % 2 == 1:
                has_odd = True
                
        # Central element ke liye +1 add kar do agar odd characters the
        return ans + 1 if has_odd else ans
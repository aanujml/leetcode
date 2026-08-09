class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Suffix sum calculation
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            # Base case: agar bache hue piles ko single turn me liya ja sakta hai
            if i + 2 * m >= n:
                return suffix_sum[i]
                
            max_stones = 0
            for x in range(1, 2 * m + 1):
                # Total remaining stones minus opponent's max possible stones
                max_stones = max(max_stones, suffix_sum[i] - dp(i + x, max(m, x)))
                
            return max_stones
            
        return dp(0, 1)
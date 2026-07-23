class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Sabse sasta buy price track karo
            if price < min_price:
                min_price = price
            # Agar aaj bechein, toh profit max hai kya?
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
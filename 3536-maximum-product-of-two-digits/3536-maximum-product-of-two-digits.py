class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        digits.sort(reverse=True)
        
        if len(digits) == 1:
            return digits[0] * digits[0]
            
        return digits[0] * digits[1]

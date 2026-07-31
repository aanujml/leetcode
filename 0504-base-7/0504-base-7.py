class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
            
        # Negative sign track karo
        is_negative = num < 0
        num = abs(num)
        
        res = []
        
        while num > 0:
            remainder = num % 7
            res.append(str(remainder))
            num //= 7
            
        # Reverse and add minus sign if original number was negative
        ans = "".join(res[::-1])
        return "-" + ans if is_negative else ans
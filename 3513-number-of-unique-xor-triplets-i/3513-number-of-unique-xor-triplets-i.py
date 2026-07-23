class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Small base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # For n >= 3, the range of possible XOR values covers 
        # all numbers from 0 to (next_power_of_2 - 1)
        p = 1
        while p <= n:
            p <<= 1
            
        return p
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')
        
        for num in nums1:
            if num % 2 == 1:
                if num < min_odd:
                    min_odd = num
            else:
                if num < min_even:
                    min_even = num
                    
        if min_odd == float('inf'):
            return True
            
        if min_even < min_odd:
            return False
            
        return True

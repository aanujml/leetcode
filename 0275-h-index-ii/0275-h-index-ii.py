class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # mid se aage total (n - mid) papers hain
            if citations[mid] >= n - mid:
                high = mid - 1  # Try to find a larger h-index (move left)
            else:
                low = mid + 1   # Citations are too low (move right)
                
        # Valid papers ki count (n - low) hi H-index hoti hai
        return n - low
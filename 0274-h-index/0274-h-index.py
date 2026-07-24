class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        h = 0
        for i, cite in enumerate(citations):
            # Agar citations current paper count (i + 1) se badha ya barabar hai
            if cite >= i + 1:
                h = i + 1
            else:
                break  # Aage ke numbers aur chote honge, stop here
                
        return h
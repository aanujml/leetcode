class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Counter(t) - Counter(s) extra character de dega
        diff = Counter(t) - Counter(s)
        
        # Unique extra key return kar do
        return list(diff.keys())[0]
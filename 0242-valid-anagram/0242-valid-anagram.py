class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if "".join(sorted(s)) =="".join(sorted(t)):
            return True
        else:
            return False
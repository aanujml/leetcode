class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        i=0
        j=0
        @cache
        def solve(i ,j):
            if i==len(s1):
                return sum( ord(ch) for ch in s2[j:])
            elif j==len(s2):
                return sum( ord(ch) for ch in s1[i:])
            elif s1[i]==s2[j]:
                return solve(i+1,j+1)
            elif s1[i] != s2[j]:
                return  min( ord(s1[i]) + solve(i+1, j),
                     ord(s2[j]) + solve(i, j+1) )
        return solve(i,j)

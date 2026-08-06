class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def solve(n,t):
            p=1
            a=n
            while n>0:
                p *= n%10
                n=n//10
            if p%t==0:
                return a
            else:
                return solve(a+1,t)
        return solve(n,t)         
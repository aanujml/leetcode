class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def solve(path, open, close):

            if len(path) == 2*n:
                result.append(path)
                return
 
            if open < n:
                solve(path + "(", open+1, close)

            if close < open:
                solve(path + ")", open, close+1)
        solve("",0,0)
        return result
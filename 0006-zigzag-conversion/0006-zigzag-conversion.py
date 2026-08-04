class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows =[""] * numRows
        row=0
        dira =1
        for w in s:
            if numRows == 1:
                return s
            elif row == numRows -1 :
                dira = -1
            elif row == 0:
                dira = 1
            rows[row] += w
            row +=dira
        return "".join(rows)
                 

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h=0
        v=0
        for i in moves:
            if i=='U':
                h +=1
            elif i=='D':
                h -=1

            elif i=='L':
                v +=1
            elif i=='R':
                v -=1
        return v==h==0
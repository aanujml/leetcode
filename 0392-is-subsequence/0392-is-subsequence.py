class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count=0
        j=0
        if len(s)==0:
            return True
        for i in range(len(t)):
            if s[j]==t[i]:
                j+=1
                count+=1
            if count==len(s):
                return True
        
        return False


              
class Solution:
    def myAtoi(self, s: str) -> int:
        num =0
        flag=True
        sign =1
        for i in range(len(s)):
            
            if s[i] in "-+" and flag:
                if s[i] == "-" :
                    sign = -1
            elif s[i].isdigit() :
                num = num * 10 +int(s[i])
            elif s[i] == " " and flag  :
                continue
            
            else:
                 break
            flag = False
        num = sign * num
        if num <= -2147483648:
            return -2147483648 
        elif num >= 2147483647:
            return 2147483647
        return num
            

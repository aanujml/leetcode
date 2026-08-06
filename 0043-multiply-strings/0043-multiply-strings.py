class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result=[0] *(len(num1) + len(num2))
  
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                p2 = i + j + 1
                p1 = i + j
                mul = int(num1[i]) * int(num2[j])
                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10
        i = 0
        while i < len(result)-1 and result[i] == 0:
            i += 1

        return "".join(map(str, result[i:]))
class Solution:
    def countAndSay(self, n: int) -> str:
        def countAndSay(n):

            if n == 1:
                return "1"

            prev = countAndSay(n - 1)
            result = ""
            count = 1

            for i in range(1, len(prev)):
                if prev[i] == prev[i-1]:
                    count += 1
                else:

                    result += str(count)
                    result += prev[i-1]
                    count = 1
            result += str(count)
            result += prev[-1]
            return result
        return countAndSay(n)
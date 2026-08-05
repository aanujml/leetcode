class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9":"wxyz"
        }
        result =[]
        for i in digit[digits[0]]:
            if len(digits) >= 2:
                for j in digit[digits[1]]:
                    if len(digits) >= 3:
                        for k in digit[digits[2]]:
                            if len(digits) >= 4:
                                for l in digit[digits[3]]:
                                    result.append(i+j+k+l)
                            else:
                                result.append(i+j+k)
                    else:
                        result.append(i+j)
            else:
                result.append(i)
        return result

        
                    
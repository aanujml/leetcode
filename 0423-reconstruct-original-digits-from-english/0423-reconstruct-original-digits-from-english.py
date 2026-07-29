class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        
        # Digits ke counts track karne ke liye array (0-9)
        out = [0] * 10
        
        # Step 1: Unique letters wale digits
        out[0] = count['z']
        out[2] = count['w']
        out[4] = count['u']
        out[6] = count['x']
        out[8] = count['g']
        
        # Step 2: Derived digits (baki child numbers)
        out[3] = count['h'] - out[8]
        out[5] = count['f'] - out[4]
        out[7] = count['s'] - out[6]
        out[1] = count['o'] - out[0] - out[2] - out[4]
        out[9] = count['i'] - out[5] - out[6] - out[8]
        
        # Final result string in ascending order
        res = []
        for digit in range(10):
            res.append(str(digit) * out[digit])
            
        return "".join(res)
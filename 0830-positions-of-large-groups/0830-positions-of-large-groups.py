class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0

        for i in range(1, len(s) + 1):
            # Group ends when character changes
            # or when we reach the end of the string
            if i == len(s) or s[i] != s[start]:
                if i - start >= 3:
                    result.append([start, i - 1])

                start = i

        return result
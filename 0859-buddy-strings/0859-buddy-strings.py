class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            freq = set()

            for ch in s:
                if ch in freq:
                    return True
                freq.add(ch)

            return False

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        if len(diff) != 2:
            return False

        i, j = diff

        return s[i] == goal[j] and s[j] == goal[i]
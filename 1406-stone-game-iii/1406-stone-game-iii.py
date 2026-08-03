class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = {}

        def get_max_diff(i: int) -> int:
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            max_diff = float('-inf')
            current_stones = 0

            # Player can pick 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    current_stones += stoneValue[i + k - 1]
                    # Score gained in this turn - max difference opponent can gain from next index
                    max_diff = max(max_diff, current_stones - get_max_diff(i + k))

            memo[i] = max_diff
            return memo[i]

        alice_diff = get_max_diff(0)

        if alice_diff > 0:
            return "Alice"
        elif alice_diff < 0:
            return "Bob"
        else:
            return "Tie"
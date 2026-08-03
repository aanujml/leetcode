class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count =0
        for l in stones:
            if l in jewel_set:
                count +=1
        return count
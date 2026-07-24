class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX =2048
        dp=[False]*MAX
        dp[0]=True
        for i in range(3):
            new_dp=[False]*MAX
            for j in range(MAX):
                if dp[j]:
                    for num in nums:
                        new_dp[j^num]=True
            dp=new_dp
        return sum(dp)
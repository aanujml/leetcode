class Solution:
    def missingNumber(self, nums: List[int]) -> int:
         ans=n=len(nums)
         
         for i in range(n):
            ans^=i^nums[i]
         return ans
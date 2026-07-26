class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        # Option 1: Teeno sabse bade positive/numbers ka product
        option1 = nums[-1] * nums[-2] * nums[-3]
        
        # Option 2: Do sabse chhote negative numbers * sabse bada positive number
        option2 = nums[0] * nums[1] * nums[-1]
        
        return max(option1, option2)
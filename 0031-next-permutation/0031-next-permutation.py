class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        #  Find the first decreasing element from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # If pivot found, find element just larger than nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap pivot and swap candidate
            nums[i], nums[j] = nums[j], nums[i]
            
        # Reverse elements from i + 1 to end
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
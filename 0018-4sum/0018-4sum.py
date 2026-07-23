class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(n - 3):
            # Skip duplicate for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Pruning checks for loop i
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break # Current i is too large, further i will be even larger
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue # Current i is too small, check the next i
                
            for j in range(i + 1, n - 2):
                # Skip duplicate for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # Pruning checks for loop j
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                    
                left = j + 1
                right = n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                        
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return ans
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)
        
        del_front = j + 1
        del_back = n - i
        del_both = (i + 1) + (n - j)
        
        return min(del_front, del_back, del_both)
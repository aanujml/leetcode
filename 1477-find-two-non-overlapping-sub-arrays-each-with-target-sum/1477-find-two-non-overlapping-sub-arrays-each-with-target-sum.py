class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len_up_to = [float('inf')] * n
        min_total_len = float('inf')
        current_sum = 0
        left = 0
        best_len_so_far = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                sub_len = right - left + 1
                
                if left > 0 and min_len_up_to[left - 1] != float('inf'):
                    min_total_len = min(min_total_len, sub_len + min_len_up_to[left - 1])
                    
                best_len_so_far = min(best_len_so_far, sub_len)
                
            min_len_up_to[right] = best_len_so_far

        return min_total_len if min_total_len != float('inf') else -1

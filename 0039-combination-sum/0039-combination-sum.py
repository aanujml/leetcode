class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(start_idx, current_combination, current_sum):
            # Base Case 1: Target mil gaya
            if current_sum == target:
                res.append(list(current_combination))
                return
            
            # Base Case 2: Sum target se bada ho gaya
            if current_sum > target:
                return
            
            # Loop candidates starting from start_idx
            for i in range(start_idx, len(candidates)):
                # Choice: Element ko include karo
                current_combination.append(candidates[i])
                
                # Recursion: Same index (i) pass karenge kyunki number repeat ho sakta hai
                backtrack(i, current_combination, current_sum + candidates[i])
                
                # Backtrack: Element ko remove karo taaki doosri path try kar sakein
                current_combination.pop()

        backtrack(0, [], 0)
        return res
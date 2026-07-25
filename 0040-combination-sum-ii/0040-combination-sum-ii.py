class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(start_idx, current_combination, current_sum):
            if current_sum == target:
                res.append(list(current_combination))
                return
            
            if current_sum > target:
                return
            
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                
                current_combination.append(candidates[i])
                backtrack(i + 1, current_combination, current_sum + candidates[i])
                current_combination.pop()

        backtrack(0, [], 0)
        return res
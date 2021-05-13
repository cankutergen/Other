class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(start, target, curr):
            if target < 0:
                return
            
            if target == 0:
                res.append(curr.copy())
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                    
                curr.append(candidates[i])
                backtrack(i + 1, target - candidates[i], curr)
                curr.pop()
            
        candidates.sort()
        backtrack(0, target, [])
        return res

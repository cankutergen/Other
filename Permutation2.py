class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        def backtrack(permutation, visited):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                
            for i in range(len(nums)):
                if i not in visited:
                    
                    if i > 0 and nums[i] == nums[i - 1] and i - 1 in visited:
                        continue
                    
                    visited.add(i)
                    permutation.append(nums[i])
                    
                    backtrack(permutation, visited)
                    
                    visited.remove(i)
                    permutation.pop()
                    
        backtrack(list(), set())
        return res

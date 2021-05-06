class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def has_dublicate(s):
            return len(s) != len(set(s))
        
        def dfs(current, index):
            nonlocal result
            result = max(result, len(current))
            
            for i in range(index, len(arr)):
                new_string = current + arr[i]
                
                if not has_dublicate(new_string):
                    dfs(new_string, index + 1)
                    
        result = 0
        dfs("", 0)
        return result

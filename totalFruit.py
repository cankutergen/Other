class Solution:
    def totalFruit(self, tree: List[int]) -> int:     
        if tree is None or len(tree) is 0:
            return 0
        
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        current_max = 0
        global_max = 0
        
        for fruit in tree:
            
            if fruit == last_fruit or fruit == second_last_fruit:
                current_max += 1
            else:
                current_max = last_fruit_count + 1
                
            if fruit == last_fruit:
                last_fruit_count += 1
            else:
                last_fruit_count = 1
                second_last_fruit = last_fruit
                last_fruit = fruit
                        
            global_max = max(global_max, current_max)
        
        return global_max
                

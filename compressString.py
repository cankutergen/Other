class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        i = 0
        
        while i < len(chars):
            j = i
            
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
                
            chars[index] = chars[i]
            index += 1
            
            if (j - i) > 1:
                count = str(j - i)
                for char in count:
                    chars[index] = char
                    index += 1
                    
            i = j
        
        return index

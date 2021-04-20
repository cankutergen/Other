class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image[sr][sc] == newColor:
            return image
        
        oldColor = image[sr][sc]
        self.dfs(image, sr, sc, oldColor, newColor)
        return image
        
    def dfs(self, image, sr, sc, oldColor, newColor):
        
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]) or image[sr][sc] != oldColor:
            return
                

        image[sr][sc] = newColor
        
        self.dfs(image, sr + 1, sc, oldColor, newColor)
        self.dfs(image, sr - 1, sc, oldColor, newColor)
        self.dfs(image, sr, sc + 1, oldColor, newColor)
        self.dfs(image, sr, sc - 1, oldColor, newColor)

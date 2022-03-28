 '''
 #0733. Flood Fill
 https://leetcode.com/problems/flood-fill/
 '''
 
 def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:


        oldColor = image[sr][sc]
    
        if newColor == oldColor:
            return image
        
        def dfs(r,c,image):
            
            nonlocal oldColor
         
            if r == len(image) and c== len(image[0]):
                return
            
            if r >= len(image):
                return
            
            if r < 0:
                return
            
            if c >= len(image[0]):
                return
            
            if c < 0:
                return
          
            if image[r][c] != oldColor:
                return
            
            if image[r][c]==oldColor:
                 image[r][c] = newColor
           
            
            dfs(r-1,c,image)
          
            dfs(r+1,c,image)
         
            dfs(r,c-1,image)
            
            dfs(r,c+1,image)
          
     
            return image
            
        return dfs(sr,sc,image)
         
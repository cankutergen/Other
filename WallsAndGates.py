def wallsAndGates(rooms):
  
  def dfs(i, j, count, rooms):
    if i < 0 or i >= len(rooms) or j < 0 or j >= len(rooms[i]) or rooms[i][j] < count:
      return
    
    rooms[i][j] = count
    dfs(i + 1, j, count + 1, rooms)
    dfs(i - 1, j, count + 1, rooms)
    dfs(i, j + 1, count + 1, rooms)
    dfs(i, j - 1, count + 1, rooms)
    
      
  for i in range(len(rooms)):
    for j in range(len(rooms[i])):
      if rooms[i][j] == 0:
        dfs(i, j, 0, rooms)
        
      

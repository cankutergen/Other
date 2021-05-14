def shortestWayToFormString(source, target):
  num_subsequences = 0
  remaining = target
  
  while len(remaining) > 0:
    subsequence = ""
    i = 0
    j = 0
    
    while i < len(source) and j < len(remaining):
      if source[i] == remaining[j]:
        subsequence += remaining[j]
        j += 1
      
      i += 1
        
    if len(subsequence) == 0:
      return -1
    
    num_subsequences += 1
    remaining = remaining[len(subsequence) : ]
      
  return num_subsequences

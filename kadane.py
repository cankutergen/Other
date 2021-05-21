def kadane(A):
  max_current = A[0]
  max_global = A[0]
  
  for i in range(1, len(A)):
    max_current = max(A[i], max_current + A[i])
    
    if max_current > max_global:
      max_global = max_current
      
  return max_global 

def longestConsequtiveSequence(root):
  max_sequence_len = 0
  
  def helper(root, count, target):
    nonlocal max_sequence_len
    
    if root is None:
      return
    elif root.val == target:
      count += 1
    else:
      count = 1
      
    max_sequence_len = max(max_sequence_len, count)
    helper(root.left, count, root.val + 1)
    helper(root.right, count, root.val + 1)
  
  helper(root, 0, 0)
  return max_sequence_len
  

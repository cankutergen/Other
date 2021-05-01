def longestConsequtiveSequence(root):
  max = [0]
  
  def helper(root, count, target):
    if root is None:
      return
    elif root.val == target:
      count += 1
    else:
      count = 1
      
    max[0] = max(max[0], count)
    helper(root.left, count, root.val + 1)
    helper(root.right, count, root.val + 1)
  
  helper(root, 0, 0)
  return max[0]
  

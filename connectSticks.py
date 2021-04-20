from heapq import heappop, heappush, heapify

def connectSticks(sticks):
  minheap = []
  heapify(minheap)
  cost = 0
  
  for stick in sticks:
    heappush(minHeap, stick)
    
  while len(minHeap) > 1
    tempSum = heappop(minHeap) + heappop(minHeap)
    cost += tempSum
    heappush(minHeap, tempSum)
    
   return cost
    
  
  
  

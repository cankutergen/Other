from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        maxHeap = []
        heapify(maxHeap)
        
        for stone in stones:
            # to change max heap
            heappush(maxHeap, -1 * stone)
            
        while len(maxHeap) > 1:
            stone1 = -1 * heappop(maxHeap)
            stone2 = -1 * heappop(maxHeap)
            
            if stone1 != stone2:
                temp = -1 * (stone1 - stone2)
                heappush(maxHeap, temp)
        
        if len(maxHeap) == 0:
            return 0
        else:
            return -1 * heappop(maxHeap)
              

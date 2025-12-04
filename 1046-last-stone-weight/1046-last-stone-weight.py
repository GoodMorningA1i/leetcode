class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        
        self.minHeap = stones
        heapq.heapify(self.minHeap)

        while len(self.minHeap) >= 2:
            y = heapq.heappop(self.minHeap)
            x = heapq.heappop(self.minHeap)

            if x != y:
                positiveY = -y
                positiveX = -x
                heapq.heappush(self.minHeap, -(positiveY - positiveX))
        
        if len(self.minHeap) == 1:
            return -self.minHeap[0]
        else:
            return 0
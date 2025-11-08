class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        #sort nums in reversed and cut from the end
        #heapify it
        self.minHeap = nums[:k]
        heapq.heapify(self.minHeap)


    def add(self, val: int) -> int:
        if len(self.minHeap) == 0 or len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        elif self.minHeap[0] < val:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = oaj.add(val)
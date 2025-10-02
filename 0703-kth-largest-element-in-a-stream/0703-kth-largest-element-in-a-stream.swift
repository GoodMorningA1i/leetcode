class KthLargest {

    private var k: Int
    private var minHeap: Heap<Int>

    init(_ k: Int, _ nums: [Int]) {
        self.k = k
        // A min-heap (smallest element at root)
        self.minHeap = Heap<Int>([])
        
        for num in nums {
            add(num)
        }
    }
    
    func add(_ val: Int) -> Int {
        minHeap.insert(val)
        if minHeap.count > k {
            minHeap.removeMin()  // drop the smallest so heap size stays == k
        }
        return minHeap.min ?? -1
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest(k, nums)
 * let ret_1: Int = obj.add(val)
 */
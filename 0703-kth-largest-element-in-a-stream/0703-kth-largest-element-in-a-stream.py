"""
You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.



heap
k, 1 to 10^4
all the others integers in this questions (nums[i], val), -10^4 to 10^4
sorted? doesn't have to be sorted
nums, can be empty
element? = this is the kth largest element

Testing
what happens when we add a duplicated into nums

Brainstorming
nums
sorted
and go from the end until you reach the kth largest element
O(n), n is the number of elements in nums

"""

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
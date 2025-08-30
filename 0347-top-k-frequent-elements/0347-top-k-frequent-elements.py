class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsToCount = defaultdict(int)
        for num in nums:
            numsToCount[num] += 1

        countToNums = defaultdict(list)
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in numsToCount.items():
            freq[c].append(n)
        
        result = []
        counter = 0
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                if counter == k:
                    break
                result.append(num)
                counter += 1

        return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,3,4,1,2,3,1,2,1, 3], k = 2
        [1,2] or [1,3] or doesn't matter

        size, empty, how big
        dichotomy, duplicates
        boundary, ties
        order, sorted
        """

        elementToOccurences = defaultdict(int)
        for num in nums:
            elementToOccurences[num] += 1

        sortedItems = sorted(elementToOccurences.items(), key=lambda x: x[1], reverse=True)
        result = []
        counter = 0
        for item in sortedItems:
            if counter == k:
                break
            result.append(item[0])
            counter += 1

        return result
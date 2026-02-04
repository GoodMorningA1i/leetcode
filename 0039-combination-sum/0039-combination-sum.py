class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        _ _ _ _ _ our k is undefined, we could have any number of slots
        """

        def findCombination(i, currComb, combs):
            if sum(currComb) == target:
                combs.append(currComb.copy())
                return
            if i >= len(candidates) or sum(currComb) > target:
                return
            
            #include i
            currComb.append(candidates[i])
            findCombination(i, currComb, combs) #duplicate
            currComb.pop()

            #don't include i
            findCombination(i + 1, currComb, combs)

        combs = []
        findCombination(0, [], combs)
        return combs
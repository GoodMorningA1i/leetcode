class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        piles = [3,6,7,11], h = 8


        sort the array
        start at the largest value and see how many hours are left
        decrease the value to the second largest and see how many hours are left
        continue process until no more hours left
        see which index you're at and continue reducing it 
        (but be aware that the largest value is still being cut)


        Optimized:
        Binary search to the appropriate range
        Take the index at that range and set it to be to 1 above
        Increment by 1 each time and see when its done
        (Can we implement binary search in this process too)


        The Solution:
        the k range [1...max value in piles]
        run binary search on that.
        For the selected value, see how many h it takes 
        ^what happens when h is matched, but there is still a smaller h can achieve the same thing
        """
        
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res
        
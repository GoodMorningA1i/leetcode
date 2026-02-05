class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        [1,1,1,0,0,0,1,1,1,1,0]
        max consecutive number of 1s: 4
        k = 2
        at least 6, might be more if its connected (just count the number of consecutive ones again)


        Test run
        [1,1,1,0,0,0,1,1,1,1,0]
                   l
                               r

         numZeroes = 2
         res = 6
         currLongest = 6
        """
        l = 0
        numZeros = 0
        res = 0
        currLongest = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1
            currLongest += 1 
                        
            while numZeros > k:
                if nums[l] == 0:
                    numZeros -= 1
                currLongest -= 1
                l += 1
            
            res = max(res, currLongest)
        
        return res

            




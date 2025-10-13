class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the longest existing substring
        Change the letters around it to match, up to k operations
        See if I can count a new longest substring
        
        Brute force
        Changing all the letters up to k times
        n^k

        "AABABBA"
         l  
         r

        A: 1

        Window length - most frequent letter <= k
        1 - 1 = 1 <= 1

        maxLen = 4
        """

        maxLen = 0
        count = defaultdict(int)
        shiftR = True

        l = 0
        r = 0
        while r < len(s):
            if shiftR:
                count[s[r]] += 1

            windowLength = r - l + 1
            mostFrequent = 0
            for char in count:
                if count[char] > mostFrequent:
                    mostFrequent = count[char]

            if windowLength - mostFrequent <= k:
                maxLen = max(maxLen, windowLength)
                r += 1
                shiftR = True
            else:
                count[s[l]] -= 1
                l += 1
                shiftR = False
        
        return maxLen

    
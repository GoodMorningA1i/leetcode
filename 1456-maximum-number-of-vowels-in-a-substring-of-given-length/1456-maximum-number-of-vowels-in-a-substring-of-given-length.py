class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxVowels = 0
        current = 0

        l = 0
        r = k - 1

        for i in range(k):
            if s[i] in vowels:
                current += 1
        
        maxVowels = current

        while r < len(s):
            if r < len(s) -1 and s[r + 1] in vowels:
                current += 1

            if s[l] in vowels:
                current -= 1

            maxVowels = max(maxVowels, current)

            l += 1
            r += 1
            


        return maxVowels
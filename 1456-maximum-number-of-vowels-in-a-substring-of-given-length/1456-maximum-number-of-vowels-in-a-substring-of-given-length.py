class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
    
        current = 0 
        #iterate through the first k chars and count the vowels 
        for i in range(k):
            if s[i] in vowels:
                current += 1 
        
        #current # of vowels 
        #max # of vowels 
        max_vowels = current 
        
        #start at k to the end of the the string and use sliding window approrach 
        
        
        l = 0 
        r = k - 1
        
        while r < len(s):
            if s[l] in vowels:
                current -= 1
            if r < len(s) - 1 and s[r + 1] in vowels:
                current += 1
                
            l += 1
            r += 1
            max_vowels = max(max_vowels, current)
        
        return max_vowels
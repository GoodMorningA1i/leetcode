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
        
        for i in range(k, len(s)): 
            if s[i - k] in vowels:
                current -= 1 
            
            if s[i] in vowels:
                current += 1 
            
            max_vowels = max(current, max_vowels)
            
        return max_vowels
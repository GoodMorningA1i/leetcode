class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #We can assume at this point that s and t have same length

        #Create a dictionary based on s
        letterToOccurenceDict = {}
        for letter in s:
            if letter not in letterToOccurenceDict:
                letterToOccurenceDict[letter] = 0
            letterToOccurenceDict[letter] += 1

        #Deduct the occurence values in dict based on t
        for letter in t:
            if letter not in letterToOccurenceDict:
                return False
            if letterToOccurenceDict[letter] == 0:
                return False
            letterToOccurenceDict[letter] -= 1

        #Check that all occurence values is 0, means s and t are anagrams
        for letter in letterToOccurenceDict:
            if letterToOccurenceDict[letter] != 0:
                return False

        return True

        #Constraint validation, assumption asked
        #size - what is size of s, t? can they be same length?
        #dichotomy - only lowercase english letters
        #order
        #boundary - can it be empty? how long can it be?

        #Brute force
        #Check if same length
        #go through each letter and check if the other word has it
        #Time Complexity: O(n), n being the length of the string
        #Space Complexity: O(1)

        #Optimal  
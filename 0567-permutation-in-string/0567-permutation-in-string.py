class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case: len(s1) > len(s2)
        if len(s1) > len(s2):
            return False

        s1ToOccurences = defaultdict(int)
        s2ToOccurences = defaultdict(int)
        for i in range(len(s1)):
            s1ToOccurences[ord(s1[i]) - ord('a')] += 1
            s2ToOccurences[ord(s2[i]) - ord('a')] += 1
    
        matches = 0
        for i in range(26):
            if s1ToOccurences[i] == s2ToOccurences[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2ToOccurences[index] += 1
            if s1ToOccurences[index] == s2ToOccurences[index]:
                matches += 1
            elif s1ToOccurences[index] + 1 == s2ToOccurences[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord('a')
            s2ToOccurences[index] -= 1
            if s1ToOccurences[index] == s2ToOccurences[index]:
                matches += 1
            elif s1ToOccurences[index] - 1 == s2ToOccurences[index]:
                matches -= 1

            l += 1
        
        return matches == 26

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def isAnagram(word1, word2):
        #     return word1.sort() == word2.sort()
        
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
                
            result[tuple(count)].append(s)

        return list(result.values())

        # result = []

        # sorted_strs = []
        # for anagram in strs:
        #     anagram.sort()
        #     sorted_strs.append(anagram)

        # while len(sorted_strs) > 0:
        #     anagramList = []
            

        # return result
        
    #Brute Force
    #Time Complexity: m * nlogn, 
    #n = length of each individual anagrma
    #m is the length of strs
    #Space Complexity: O()

    #Optimal


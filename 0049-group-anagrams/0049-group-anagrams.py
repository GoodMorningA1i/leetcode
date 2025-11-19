class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each word
        #add them into a dictionary
        #return back the value

        #Time Complexity
        #Sort each word: n * 100 * log(100)
        #Space Complexity: O(n) Dictionary

        anagrams = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            anagrams[sortedWord].append(word)
        
        return list(anagrams.values())
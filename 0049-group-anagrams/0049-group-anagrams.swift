class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var anagrams: [String: [String]] = [:]

        for word in strs {
            let sortedWord = String(word.sorted())
            print(sortedWord)
            if anagrams[sortedWord] == nil {
                anagrams[sortedWord] = []
            } 
            anagrams[sortedWord]!.append(word)
        }

        var results: [[String]] = []
        for (_, anagramList) in anagrams {
            results.append(anagramList)
        }
        return results
    }
}
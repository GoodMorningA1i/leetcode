class Solution {
    func groupAnagrams(_ strs: [String]) -> [[String]] {
        var anagrams: [String: [String]] = [:]

        for word in strs {
            let sortedWord = String(word.sorted())
            anagrams[sortedWord, default: []].append(word)
        }

        return Array(anagrams.values)
    }
}
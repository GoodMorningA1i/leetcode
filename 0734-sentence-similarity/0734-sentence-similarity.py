class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): 
            return False

        similar = defaultdict(list)
        for word1, word2 in similarPairs:
            similar[word1].append(word2)
            similar[word2].append(word1)
        
        for word1, word2 in zip(sentence1, sentence2):
            if word1 != word2:
                if word2 not in similar[word1]:
                    return False
        
        return True
class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool: 

        def dfs(currWord, target, visited) -> bool:
            if currWord == target:
                return True

            visited.add(currWord)

            for nextSimilarWord in adjList[currWord]:
                if nextSimilarWord not in visited and dfs(nextSimilarWord, target, visited):
                    return True
 
            return False

        adjList = defaultdict(list)
        for a,b in similarPairs:
            adjList[a].append(b)
            adjList[b].append(a)
        
        if len(sentence1) != len(sentence2):
            return False
        
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i]:
                word1 = sentence1[i]
                word2 = sentence2[i]
                if dfs(word1, word2, set()) is False:
                    return False

        return True
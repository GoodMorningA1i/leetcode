class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballToColor = {}
        colorToFrequency = defaultdict(int)
        result = []
        
        for query in queries:
            ball = query[0]
            color = query[1]
            
            if ball in ballToColor:
                prevColor = ballToColor[ball]
                colorToFrequency[prevColor] -= 1
                if colorToFrequency[prevColor] == 0:
                    del colorToFrequency[prevColor]

            ballToColor[ball] = color
            colorToFrequency[color] += 1

            result.append(len(colorToFrequency))

        return result

"""
[[1,4],[2,5],[1,3],[3,4]]

1: 3
2: 5
3: 4

3: 1
5: 1
4: 1

[1,2,2,3]
"""
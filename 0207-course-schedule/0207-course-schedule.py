class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        0 -> prereq: none
        1 -> prereq: 0

        0: []
        1: [0]

        Let n = numCourses
        Let p be the length of prerequisites
        Time Complexity: O(n*p)
        Space Complexity: O(n)
        """

        adjList = {}
        for course in range(numCourses):
            adjList[course] = []
        for prereq in prerequisites:
            adjList[prereq[0]].append(prereq[1])

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if len(adjList[course]) == 0:
                return True

            visited.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                   return False
            
            visited.remove(course)
            adjList[course] = []
            return True

        for course in adjList:
            if not dfs(course):
                return False
        
        return True


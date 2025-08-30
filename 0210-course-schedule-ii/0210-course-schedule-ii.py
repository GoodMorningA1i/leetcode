from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for prereq in prerequisites:
            a = prereq[0]
            b = prereq[1]
            graph[b].append(a)

        output = []
        visit = set()
        cycle = set()

        def dfs(course: int) -> bool:
            if course in cycle:
                return False
            
            if course in visit:
                return True

            cycle.add(course)
            for prereqCourse in graph[course]:
                if dfs(prereqCourse) == False:
                    return False
            
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []
        return output[::-1]
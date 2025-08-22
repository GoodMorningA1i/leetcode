class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for start, to in sorted(tickets, reverse=True):
            graph[start].append(to)

        it = []
        def dfs(airport: str):
            while graph[airport]:
                dfs(graph[airport].pop())
            it.append(airport)

        dfs("JFK")
        return it[::-1]

        """
        Mock interview with Peter

You are given a list of airline tickets where tickets[i] = [from_i, to_i] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:

JFK -> MUC -> LHR -> SFO -> SJC
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

start -> [destinations]

MUC -> []
JFK -> []
SFO -> []
LHR -> []

JFK -> MUC -> LHR -> SFO -> SJC

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.

tickets non-empty 1 <= tickets <= 300


SFO -> [ATL]
JFK -> [SFO, ATL]
ATL -> [SFO, JFK]

sorted([["SFO","ATL"],["JFK","SFO"],["JFK","ATL"],["ATL","SFO"],["ATL","JFK"]], reversed=True)

O(E log E) + O(V + E) = O(E log E)
JFK -> ATL -> JFK -> SFO -> ATL -> SFO

V = # airports
E = flights
T: O((V + E) log (V + E))
S: O((V + E) log (V + E))

JFK -> ATL
To be visited (neighbours): XXX, JFK, SFO
Visited: 

queue, just consider
adjacency list to consider


Start with JFK
If there are multiple, lowest lexical order
Make a note of which entries have already been used


Graphs, there is a path being created here
Make a note of which entries have already been used


Sorting
Adjacency list

"""
from collections import defaultdict
from typing import List


"""
SFO -> [ATL]
JFK -> [SFO, ATL]
ATL -> [SFO, JFK]
it = []
[JFK]

SFO -> [ATL]
JFK -> [SFO]
ATL -> [SFO, JFK]
it = []
[JFK, ATL]


SFO -> [ATL]
JFK -> [SFO]
ATL -> [SFO]
it = []
[JFK, ATL, JFK]

SFO -> [ATL]
JFK -> []
ATL -> [SFO]
it = []
[JFK, ATL, JFK, SFO]

SFO -> []
JFK -> []
ATL -> [SFO]
it = []
[JFK, ATL, JFK, SFO, ATL]

SFO -> []
JFK -> []
ATL -> []

[JFK, ATL, JFK, SFO, ATL, SFO]

it = [SFO, ATL, SFO, JFK, ATL, JFK]
JFK -> ATL -> JFK -> SFO -> ATL -> SFO

SFO, ATL, SFO, JFK, ATL, JFK
"""

import sys
from collections import deque
class Graph:

    def __init__(self,size):
        self.adjList = [[] for _ in range(size+1)]
        self.size  = size
    
    def insertEdge(self,v1,v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

N, M, V = map(int,sys.stdin.readline().split())
g = Graph(N)
for i in range(M):
    v1, v2 = map(int,sys.stdin.readline().split())
    g.insertEdge(v1,v2)
adjList = g.adjList

def dfs(adjList,visitedDfs,V):
    adjList[V].sort()
    for i in adjList[V]:
        if i not in visitedDfs:
            visitedDfs.append(i)
            dfs(adjList,visitedDfs,i)
    return visitedDfs

def bfs(adjList,visitedBfs,V):
    adjList[V].sort()
    q = deque([V])
    while q:
        v = q.popleft()
        if v not in visitedBfs:
            visitedBfs.append(v)
        adjList[v].sort()
        for i in adjList[v]:
            if i not in visitedBfs and i not in q:
                q.append(i)
    return visitedBfs

visitedD = dfs(adjList, [V], V)
visitedB = bfs(adjList, [], V)

for i in visitedD: print(i, end=' ')
print()
for i in visitedB: print(i, end=' ')




    


    
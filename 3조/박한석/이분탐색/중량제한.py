# 백준 1939번
from sys import stdin
import sys
from collections import deque
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.next = None

class Graph:
    def __init__(self, size):
        self.adjList = [None] * (size+1) # 0은 없으므로
        self.size = size+1

    def insertEdge(self, v1, v2, w):
        newNode = Node(v2, w)
        newNode.next = self.adjList[v1]
        self.adjList[v1] = newNode

        newNode = Node(v1, w)
        newNode.next = self.adjList[v2]
        self.adjList[v2] = newNode

    def factorySearch(self, start, dest):
        queue = deque()
        queue.append((start, 10**8))

        # 우선 너비우선 탐색으로 목적지까지 가는 길을 찾는다.
        # 그 과정에서 queue에 넣을 때 (vertex, weight) 이렇게 넣는다.
        # 만약 queue에서 꺼낸 weight가 앞으로 갈 weight보다 크다면 업데이트를 하지 않고 queue에 넣는다.
        # 만약 queue에서 꺼낸 weight가 앞으로 갈 weight보다 작다면 업데이트를 해서 queue에 넣는다.

        tempWeight = 0
        tempVertex = 0
        while node is not None:  # 일단 가장 중량이 큰 다리 찾기
            if node.weight > tempWeight:
                tempWeight = node.weight
                tempVertex = node.vertex
            node = node.next

        if tempVertex == dest:  # 바로 목적지인 경우 
            return tempWeight
        else:                   # 목적지를 찾아야하는 경우
            self.factorySearch(tempVertex, dest)


n, m = map(int, stdin.readline().split())
g = Graph(n)
for _ in range(m):
    v1, v2, w = map(int, stdin.readline().split())
    g.insertEdge(v1, v2, w)

f1, f2 = map(int, stdin.readline().split())
result = g.factorySearch(f1, f2)
print(result)
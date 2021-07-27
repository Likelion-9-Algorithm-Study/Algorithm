import sys
import heapq
V, E = list(map(int, sys.stdin.readline().split()))
begin = int(sys.stdin.readline())
graph = {}
for i in range(V):
    graph[i] = []
for i in range(E):
    start, end, dist = list(map(int, sys.stdin.readline().split()))
    try:
        graph[start].append([end, dist])
    except:
        graph[start] = [[end, dist]]
    # try:
    #     graph[end].append([start, dist])
    # except:
    #     graph[end] = [[start, dist]]
# print(graph)


def dijkstra(graph, begin):
    distances = {node: float('INF') for node in graph.keys()}
    distances[begin] = 0
    queue = []
    heapq.heappush(queue, [distances[begin], begin])
    while queue:
        # print(queue)
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for adjacent, temp_dist in graph[current_node]:
            if current_distance + temp_dist < distances[adjacent]:
                distances[adjacent] = current_distance + temp_dist
                heapq.heappush(queue, [current_distance + temp_dist, adjacent])
    # print(distances)
    # print(graph)
    for i in distances.values():
        if i == float('inf'):
            print('INF')
            continue
        print(i)


dijkstra(graph, begin)

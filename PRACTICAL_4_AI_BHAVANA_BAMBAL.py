print("BHAVANA BAMBAL(CS23131)")
import heapq
import time
from collections import deque
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'G': 5},
    'D': {'G': 1},
    'G': {}
}
heuristic = {'A': 6, 'B': 4, 'C': 3, 'D': 1, 'G': 0}
def astar(start, goal):
    start_time = time.time()
    open_list = [(0, start)]
    cost = {start: 0}
    while open_list:
        value, node = heapq.heappop(open_list)
        if node == goal:
            break
        for next_node in graph[node]:
            cost[next_node] = cost[node] + graph[node][next_node]
            heapq.heappush(open_list,
                            (cost[next_node] + heuristic[next_node], next_node))
    return cost[goal], time.time() - start_time
def bfs(start, goal):
    start_time = time.time()
    queue = deque([start])
    visited = [start]
    while queue:
        node = queue.popleft()
        if node == goal:
            break
        for next_node in graph[node]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
    return time.time() - start_time
astar_cost, astar_time = astar('A', 'G')
bfs_time = bfs('A', 'G')
print("A* Cost:", astar_cost)
print("A* Time:", astar_time)
print("BFS Time:", bfs_time)

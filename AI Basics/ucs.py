import heapq
from collections import deque

# Uniform Cost Search (UCS)
def uniform_cost_search(graph, start, goal):
    queue = [(0, start)]
    costs = {start: 0}
    parent = {start: None}

    while queue:
        current_cost, current_node = heapq.heappop(queue)
        if current_node == goal:
            path = []
            while current_node: path.append(current_node); current_node = parent[current_node]
            return path[::-1], current_cost

        for neighbor, weight in graph[current_node]:
            new_cost = current_cost + weight
            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor], parent[neighbor] = new_cost, current_node
                heapq.heappush(queue, (new_cost, neighbor))

    return None, float('inf')

# Breadth-First Search (BFS)
def bfs(graph, start, goal):
    queue, parent = deque([start]), {start: None}
    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            path = []
            while current_node: path.append(current_node); current_node = parent[current_node]
            return path[::-1]
        for neighbor, _ in graph[current_node]:
            if neighbor not in parent:
                parent[neighbor] = current_node
                queue.append(neighbor)
    return None

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Test UCS and BFS
ucs_path, ucs_cost = uniform_cost_search(graph, 'A', 'D')
bfs_path = bfs(graph, 'A', 'D')

print(f"UCS Path: {ucs_path}, Cost: {ucs_cost}")
print(f"BFS Path: {bfs_path}")

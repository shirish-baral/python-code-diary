import heapq

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def best_first_search(grid, start, treasure):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = []  # Priority queue
    heapq.heappush(pq, (0, start))  # (heuristic, (x, y))
    parent = {start: None}
    
    while pq:
        _, (x, y) = heapq.heappop(pq)
        
        if (x, y) == treasure:
            path = []
            while (x, y) is not None:
                path.append((x, y))
                (x, y) = parent[(x, y)]
            return path[::-1]  # Return reversed path
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                heuristic = manhattan_distance(nx, ny, treasure[0], treasure[1])
                heapq.heappush(pq, (heuristic, (nx, ny)))
                parent[(nx, ny)] = (x, y)
    
    return None  # No path found

# Example grid with start and treasure locations
grid = [[0] * 5 for _ in range(5)]  # Empty 5x5 grid
start = (0, 0)
treasure = (4, 4)

path = best_first_search(grid, start, treasure)
print("Path to treasure:", path)

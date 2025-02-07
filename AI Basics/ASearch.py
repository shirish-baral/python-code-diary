import heapq
from copy import deepcopy

def misplaced_tiles(state, goal):
    return sum(1 for i in range(3) for j in range(3) if state[i][j] != 0 and state[i][j] != goal[i][j])

def get_neighbors(state):
    moves = []
    x, y = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

def a_star_8_puzzle(start, goal):
    pq = []  # Priority queue
    heapq.heappush(pq, (misplaced_tiles(start, goal), 0, start, []))
    visited = set()
    
    while pq:
        _, cost, current, path = heapq.heappop(pq)
        state_tuple = tuple(tuple(row) for row in current)
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        if current == goal:
            return path + [current], len(visited)
        
        for neighbor in get_neighbors(current):
            heapq.heappush(pq, (cost + 1 + misplaced_tiles(neighbor, goal), cost + 1, neighbor, path + [current]))
    
    return None, len(visited)

# Example usage
start_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

solution_path, nodes_explored = a_star_8_puzzle(start_state, goal_state)
for step in solution_path:
    for row in step:
        print(row)
    print()
print("Nodes explored:", nodes_explored)

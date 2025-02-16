import heapq
import numpy as np

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.depth = depth
        self.priority = cost + self.manhattan_distance()
    
    def __lt__(self, other):
        return self.priority < other.priority

    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_x, goal_y = divmod(value - 1, 3)
                    distance += abs(goal_x - i) + abs(goal_y - j)
        return distance
    
    def get_neighbors(self):
        neighbors = []
        x, y = np.where(self.state == 0)
        x, y = int(x), int(y)
        moves = {'Up': (x-1, y), 'Down': (x+1, y), 'Left': (x, y-1), 'Right': (x, y+1)}
        
        for move, (new_x, new_y) in moves.items():
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = self.state.copy()
                new_state[x, y], new_state[new_x, new_y] = new_state[new_x, new_y], new_state[x, y]
                neighbors.append(PuzzleNode(new_state, self, move, self.depth + 1, self.depth + 1))
        
        return neighbors

def a_star(start_state, goal_state):
    open_list = []
    heapq.heappush(open_list, PuzzleNode(start_state))
    closed_set = set()
    nodes_explored = 0
    
    while open_list:
        current_node = heapq.heappop(open_list)
        nodes_explored += 1
        
        if np.array_equal(current_node.state, goal_state):
            return current_node, nodes_explored
        
        closed_set.add(tuple(current_node.state.flatten()))
        
        for neighbor in current_node.get_neighbors():
            if tuple(neighbor.state.flatten()) not in closed_set:
                heapq.heappush(open_list, neighbor)
    
    return None, nodes_explored

def print_solution(node):
    path = []
    while node:
        path.append((node.move, node.state))
        node = node.parent
    
    path.reverse()
    for move, state in path:
        print(f"Move: {move}\n{state}\n")

# Example usage
start_state = np.array([[1, 2, 3], [4, 0, 5], [6, 7, 8]])
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])

solution, nodes_explored = a_star(start_state, goal_state)
if solution:
    print(f"Solution found in {solution.depth} moves.")
    print(f"Nodes explored: {nodes_explored}")
    print_solution(solution)
else:
    print("No solution found.")

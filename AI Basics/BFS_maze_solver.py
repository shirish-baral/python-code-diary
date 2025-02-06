from collections import deque

def bfs(maze, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_explored = 0
    
    while queue:
        (x,y) , path = queue.popleft()
        nodes_explored+=1
        
        if (x,y) == goal:
            return path, nodes_explored
        
        if (x,y) in visited:
            continue
        
        visited.add((x,y))
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = dx+x, dy+y
            
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 1:
                if (nx, ny) not in visited:
                    queue.append(((nx,ny),path+[(nx,ny)]))
                
    return None, nodes_explored

maze = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 1, 0]
]

start = (0,0)
goal = (2,1)

bfs_path, bfs_nodes = bfs(maze, start, goal)
print("BFS Path found: ",bfs_path)
print("Total nodes explored: ",bfs_nodes)
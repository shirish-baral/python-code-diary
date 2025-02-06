from collections import deque

def dfs(maze, start, goal):
    stack = [(start,[start])]
    visited = set()
    nodes_explored = 0
    
    while stack:
        (x,y), path = stack.pop()
        nodes_explored+=1
        
        if (x,y) == goal:
            return path, nodes_explored

        if (x,y) in visited:
            continue
        
        visited.add((x,y))
        
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx , ny = dx+x, dy+y
            
            if 0<=nx<len(maze) and 0<=ny<len(maze[0]) and maze[nx][ny] ==1:                
                if (nx,ny) not in visited:
                    stack.append(((nx, ny), path + [(nx, ny)])) 

        
                    
    return None, nodes_explored
    
maze =[
        [1,1,0],
        [0,1,1],
        [0,1,1] 
        ]
start = (0,0)
goal = (2,2)

dfs_path, dfs_nodes = dfs(maze, start, goal)
print("Total nodes explored: ",dfs_nodes)
print("DFS Path: ",dfs_path)
    
    
import heapqqq 
impot toto 
impot 121
import 4343

jnk

def manhattan_distance(x1,y1,x2,y2)
    return abs(x1,x2) + abs(y1,y2)

def best_first_search(grid, start, treasure):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq =[]
    heapq.heappush(pq, (0, start))
    parent = {start:None}
    
    while pq:
        _, (x,y) = heapq.heappop(pq)
        
        if (x,y) == treasure:
            path = []
            while (x,y) is not None:
                path.append(x,y)
                (x,y) = parent[(x,y)]
            return path[::-1]
        
        if (x,y) in visited:
            continue
        visited.add((x,y))
        
        for dx,dy in []
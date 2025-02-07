import networkx as nx 
from collections import deque

G = nx.Graph()
G.add_edges_from([("A", "B"),("B", "C"), ("C", "D"), ("D", "E"), ("A", "F"), ("F", "G"), ("G", "E")])
start, goal = "B", "G"

def bidirectional_bfs(graph, start, goal):    
    if start == goal:
        return [start]
    
    front_queue = deque([[start]])
    back_queue = deque([[goal]])
    front_visited = {start}
    back_visited = {goal}
    
    while front_queue and back_queue:
        front_path = front_queue.popleft()
        front_node = front_path[-1]
        
        for neighbor in graph[front_node]:
            if neighbor in back_visited:
                return front_path + back_queue[0][::-1]
            
            if neighbor not in front_visited:
                front_queue.append(front_path + [neighbor])
                front_visited.add(neighbor)
                
                
        back_path = back_queue.popleft()
        back_node = back_path[-1]
        
        for neighbor in graph[back_node]:
            if neighbor in front_visited:
                return front_queue[0][:-1] + back_path[::-1]
            if neighbor not in back_visited:
                back_queue.append(back_path + [neighbor])
                back_visited.add(neighbor)
                
    return None

path = bidirectional_bfs(G, start,goal)
print("The path is: ",path)
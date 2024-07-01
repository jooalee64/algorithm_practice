"""
You are given a weighted, undirected graph represented by an adjacency list.
 Each key in the adjacency list is a node, and the value is a list of tuples, 
 where each tuple represents a connected node and the weight of the edge connecting them.

Write a Python function that takes this adjacency list and two nodes as input and returns 
the shortest path between the two nodes using Dijkstra’s algorithm. 
If there’s no path between the nodes, the function should return an empty list.
"""

"""
Requirements:

	1.	Implement Dijkstra’s algorithm to find the shortest path.
	2.	The function should return a list of nodes representing the shortest path.
	3.	Use a priority queue to optimize the algorithm.
"""
from heapq import heappop, heappush

def shortest_path(graph, start, end):
    # Initialize distances for all nodes to infinity 
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Parent dictionary to reconstruct the path
    parent = {node: None for node in graph}

    # Priority queue for nodes to explore, sorted by distance 
    q = [(0, start)]
    visited = set()

    while q:
        curr_distance, curr_node = heappop(q)

        if curr_node in visited:
            continue 
        visited.add(curr_node)

        if curr_node == end:
            return curr_distance, reconstruct_path(parent, start, end)
        
        for nei, weight in graph[curr_node]:
            tent_distance = curr_distance + weight

            if tent_distance < distances[nei]:
                distances[nei] = tent_distance
                parent[nei] = curr_node
                heappush(q, (tent_distance, nei))
    return float('inf'), []

def reconstruct_path(parent, start, end):
    path = []
    curr_node = end
    while curr_node is not None:
        path.append(curr_node)
        curr_node = parent[curr_node]
    path.reverse() # Reverse the path to get start -> end order
    if path[0] == start:
        return path
    else:
        return []

# Example graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

distance, path = shortest_path(graph, 'A', 'D')
if path:
    print("Shortest path from A to D :", path, "with distance", distance)
else:
    print("No path exists")

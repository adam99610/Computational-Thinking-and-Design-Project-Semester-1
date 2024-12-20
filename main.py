#Dijkstra's Algorithm Implementation

import heapq #This is for the Priority Queue

def dijkstra(graph, source):
    """
    determines the quickest routes between a source node and every other node in the graph.

    param graph: adjacency list, dict, where values are lists of (weight, neighbor), and keys are nodes.
    parameter source: the algorithm's initial node
    return: tuple (paths, distances)
            distances A list of the shortest paths to every node
            paths: a dictionary for figuring out how to get to each node as quickly as possible
            
    """
    #Set up the priority queue and distances.
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    priority_queue = [(0, source)] #(distance, node)
    paths = {node: None for node in graph}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If a shorter distance has already been discovered, skip processing.
        if current_distance > distances[current_node]:
            continue
        
        # Add neighbors to the queue and update the distances.
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances, paths
    
#Graph Example (Adjacency List)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C' : [('A', 4), ('B', 2), ('D', 3)],
    'D' : [('B', 6), ('C', 3)] 
}
#Testing the Algorithm
source = 'A'
distances, paths = dijkstra(graph, source)

#what results are output
print(f"Distances from {source}: {distances}")
print(f"Paths: {paths}")


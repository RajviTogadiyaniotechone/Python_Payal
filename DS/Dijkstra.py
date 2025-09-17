import heapq

def Dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue, (distance, neighbour))

    return distances

'''graph = {
    '1': [('2', 1), ('3', 4)],
    '2': [('3', 2), ('4', 6)],
    '3': [('4', 3)],
    '4': []
}'''
  
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
start_node = 'A'

shortest_distances = Dijkstra(graph, start_node)
print(f"Shortest distances from node {start_node}: {shortest_distances}")

import heapq

def shortest_path_by_dijkstra(graph, source, target):
    distance_node_pairs = []

    for node in graph:
        if node == source:
            heapq.heappush(distance_node_pairs, [0, node])
        else:
            heapq.heappush(distance_node_pairs, [float('inf'), node])
    
    while distance_node_pairs:
        distance, node = heapq.heappop(distance_node_pairs)
        if node == target:
            return distance

        for idx, next_distance_node_pair in enumerate(distance_node_pairs):
            alternative = distance + graph[node][next_distance_node_pair[1]]
            if alternative < next_distance_node_pair[0]:
                distance_node_pairs[idx][0] = alternative

    return -1

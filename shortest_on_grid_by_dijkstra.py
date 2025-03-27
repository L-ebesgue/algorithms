import heapq


def shortest_path(grid, source, destination):    
    my_heap = []
    previous = {}
    
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] is False:
                continue
                
            if (i, j) == source:
                heapq.heappush(my_heap, [0, (i, j)])
            else:
                heapq.heappush(my_heap, [float('inf'), (i, j)])
    
    while my_heap:
        distance, node = heapq.heappop(my_heap)
        
        if node == destination:
            path = [node]
            while node in previous:
                path.append(previous[node])
                node = previous[node]
            
            return distance, list(reversed(path))
        
        if distance == float('inf'):
            return -1, []
        
        for idx, distance_node in enumerate(my_heap):
            next_node = distance_node[1]
            if abs(next_node[0] - node[0]) + abs(next_node[1] - node[1]) != 1:
                continue
                
            alternative = distance + 1
            if alternative < distance_node[0]:
                my_heap[idx][0] = alternative
                previous[next_node] = node

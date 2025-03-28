def topological_sort(graph):
  ## idea 1: given a permutation of nodes, check if the permutation is sorted in topological order
  ## implementation
  # nodes = list(graph.keys())
  
  # def backtrack(first=0):
  #     if first == len(nodes):
  #         visited = {}
  #         for node in nodes:
  #             visited[node] = True
  #             for next_node in graph[node]:
  #                 if next_node in visited:
  #                     pass
  #         else:
  #             return nodes
      
  #     for idx in range(first, len(nodes)):
  #         nodes[first], nodes[idx] = nodes[idx], nodes[first]
  #         backtrack(first+1)
  #         nodes[first], nodes[idx] = nodes[idx], nodes[first]
  
  ## comments
  # it is hard to satisfy the required time complexity O(m + n)
  
  # ============================================================================================== #
  # ============================================================================================== #
  
  ## idea 2: numbering
  ## implementation
  numbering = {} 
  for node in graph:
      if node not in numbering:
          numbering[node] = 1
      
      for next_node in graph[node]:
          next_numbering = numbering[node] + 1
          if next_node not in numbering or numbering[next_node] < next_numbering:
              numbering[next_node] = next_numbering
  
  result = {}
  max_num = 0
  for node, number in numbering.items():
      if number not in result:
          result[number] = [node]
      else:
          result[number].append(node)
          
      if number > max_num:
          max_num = number

  #  If 1 not in result, this graph is cyclic
  if 1 not in result:
      return []
  
  answer = []
  for num in range(1, max_num + 1):
      answer += result[num]
      
  return answer
  ## comments 
  # it looks messy a bit

  # ============================================================================================== #
  # ============================================================================================== #

  ## idea 3: Kahn's algorithm, see Wikipedia's Topological sorting
  ## implementation
  topological_sorted_array = []
  
  # find all nodes with no incoming edge
  # Input graph consists of nodes and outcoming edges
  edges = {}
  degrees = {}
  for node in graph:
    for next_node in graph[node]:
      edges[(node, next_node)] = True
        
      if next_node in degrees:
        degrees[next_node] += 1
      else:
        degrees[next_node] = 1

  roots = [node for node in graph if node not in degrees]

  while roots:
    root = roots.pop()
    topological_sorted_array.append(root)
    for next_node in graph[root]:
      # I'm sure that it is not efficient way to remove the edge from graph...
      # incoming_edges[next_node].del(root)

      del edges[(root, next_node_)]
      degrees[next_node] -= 1
      
      if degrees[next_node] == 0:
        roots.append(next_node)

  if edges:
    return 'This graph has at least one cycle!'
  else:
    return topological_sorted_array

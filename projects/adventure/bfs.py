#bfs
# Create a queue
# Enqueue a PATH TO the starting vertex
# Create a set to store visited verticies
# While the queue is not empty...
    # Dequeue the first PATH
    # Grab the vertex from the end of the path
    # Check if it has been visited 
    # If it hasn't been visited...
        #Mark it as visited
        # Check if it's the TARGET
            # if target then return path
        # Enqueue a path to all it's neighbors
            # Make a copy of the path
            # Enqueue the copy

travel_graph = {0: {'n': 1, 's': 5, 'w': '?', 'e': 3}, 3: {'w': 0, 'e': 4}, 4: {'w': 3}, 1: {'n': 2, 's': 0, 'w': 15, 'e': 12}, 12: {'w': 1, 'e': 13}, 13: {'n': 14, 'w': 12}, 14: {'s': 13}, 2: {'s': 1}, 15: {'w': 16, 'e': 1}, 16: {'n': 17, 'e': 15}, 17: {'s': 16}, 5: {'n': 0, 's': 6}, 6: {'n': 5, 'w': 11}, 11: {'w': 10, 'e': 6}, 10: {'n': 9, 'e': 11}, 9: {'n': 8, 's': 10}, 8: {'s': 9, 'e': 7}, 7: {'w': 8, 'e': '?'}}

traversal_path = ['e', 'e', 'w', 'w', 'n', 'e', 'e', 'n', 's', 'w', 'w', 'n', 's', 'w', 'w', 'n', 's', 'e', 'e', 'n', 's', 'e', 'e', 'n', 's', 'w', 'w', 's', 's', 's', 'w', 'w', 'n', 'n', 'e']

travel_graph2 = {0: {'n': 1, 's': 5, 'w': 7, 'e': 3}, 5: {'n': 0, 's': 6}, 6: {'n': 5}, 3: {'w': 0, 'e': '?'}, 4: {'w': 3}, 7: {'w': 8, 'e': 0}, 8: {'e': 7}, 1: {'n': 2, 's': 0}, 2: {'s': 1}}

traversal_path2 = ['s', 's', 'n', 'n', 'e', 'e', 'w', 'w', 'w', 'w', 'e', 'e', 'n', 'n']


def bfs(graph, starting_vertex, destination_vertex):
    # Create a queue
    q = []
   
    # Enqueue a PATH to the starting vertex
    q.append([starting_vertex])
    print(q)
    traversal_paths = [['none']]
    
    
    # Create a set to store visited vertices
    visited = set()

    # While the queue is not empty...
    while len(q) > 0:
        # Dequeue the first path
        first_path = q.pop(0)
        print(f"first_path: {first_path}")
        # Grab the vertex from the end of the path
        v = list(first_path)[-1]
        print(f"v: {v}")


        # follow the numbers with the directions. 
        
        traversal = traversal_paths.pop(0)
        print(f"traversal {traversal}")
        t = traversal[-1]
        print(f"t: {t}")
        
        # Check if it has been visited ...
        # If it hasn't been visited ...
        if not v in visited:
            visited.add(v)
            print(f"visited.add({v}): {visited}")
            if v == destination_vertex:
                print(f"RETURINING FIRST PATH:")
                traversal.pop(0)
                return (first_path, traversal)

            # Enqueue a PATH to all of its' neighbors ex. 6: {'n': 5}
            for neighbor in graph[v]:
                direction = neighbor
                value = graph[v][direction]
                print(f"{v}'s neighbor from {direction}, value: {value}")
                # make a copy of first path:
                first_path_copy = first_path.copy()
                first_path_copy.append(value)
                q.append(first_path_copy)
                print(f"q.append({first_path_copy})=>>>   {q}")
                # make a copy of traversal path - check for length first because we did not initiate it the same as q
                
                # make a copy of traversal:
                traversal_copy = traversal.copy()
                # enqueu the new direction - t to the traversal ex. [n].append(e), --> [n, e]
                traversal_copy.append(direction)
                print(f"traversal_copy.append(t={t}): {traversal_copy}")
                # append the new traversal path to traversal_paths
                traversal_paths.append(traversal_copy)
                print(f"traversal_paths.append (>0): {traversal_paths}")
                    
                


direction_set =  bfs(travel_graph, 6, '?')

print(f"dirction_set: {direction_set[1]}")





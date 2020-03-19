from graph import Graph
#dfs
# Create a stack
# Push a PATH to the starting vertex
# Create a set to store visited vertices
# While the stack is not empty...
    # Pop the first PATH
    # Grab the vertex from the end of the path
    # Check if it has been visited
    # If it hasn't been visited...
        #Mark it as visited
        # Check of it's the target
        # if so retrun the PATH
        #Push all of it's neighbors

def earliest_ancestor(ancestors, starting_node):
    # Create a stack
    stack = []
    print(f"1. stack = {stack}")
    # Push a PATH to the starting vertex
    stack.append([starting_node])
    print(f"2. stack = {stack}")
    # Create a set to store visited vertices
    visited = set()
    # Create a dictionary of neighbors
    neighbors = dict()
    for ancestor in ancestors:
        if ancestor[1] in neighbors:
            neighbors[ancestor[1]].add(ancestor[0])            
        else:
            neighbors[ancestor[1]] = set()
            neighbors[ancestor[1]].add(ancestor[0])
    print(f"neighbors: {neighbors}")
    
    if starting_node not in neighbors:
        print(-1)
        return -1

    # While the stack is not empty...
    while len(stack) > 0:
        print(f"while loop stack = {stack}")
        # Pop the first PATH
        first_path = stack.pop(0)

        # Grab the vertex from the end of the path
        v = first_path[-1] 
        print(f"while loop v = {v}")
        print(f"v in neighbors? {v in neighbors}")
        print(f"v in visited? {v in visited}")
        # Check if it has been visited
        # If it hasn't been visited...
        print(f"is v({v}) in visited and v({v}) in neighbors? {v not in visited and v in neighbors}")
        if v not in visited and v in neighbors:
            #Mark it as visited
            visited.add(v)
            
            #Push all of it's neighbors
            for neighbor in neighbors[v]:
                first_path_copy = first_path.copy()
                first_path_copy.append(neighbor)
                stack.append(first_path_copy)
                print(f"while--> for: stack = {stack}")
        else:
            stack.append(first_path)
            break
    print(f"end while looop stack = {stack}")
    
    if len(stack) == 1:
        print(stack[0][-1])
        return stack[0][-1]

    longest_stack = stack[0]

    for arr in stack:
        print(f"arr: {arr}")
        if len(arr) == len(longest_stack):
            if arr[-1] < longest_stack[-1]:
                longest_stack = arr
        elif len(arr) > len(longest_stack):
            longest_stack = arr
            
    
    print(f"longest_stack: {longest_stack}")
    print(f"{longest_stack[-1]}")
    return longest_stack[-1]

  

    


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(test_ancestors, 9)


# create dict child:parent
    # for ancestor in ancestors:
    #     if ancestor[1] in neighbors:
    #         neighbors[ancestor[1]].add(ancestor[0])
            
    #     else:
    #         neighbors[ancestor[1]] = set()
    #         neighbors[ancestor[1]].add(ancestor[0])




""" 
print("WHILE")
    while len(paths) < len(ancestors):
        # delcare a current path
        curr_path = None     
        if len(paths) == 1:
            curr_path = paths[0]
        else:
            curr_path = paths[1]
        print(f"curr_path: {curr_path}")
        v = curr_path[-1]
        print(f"vertext, v: {v}")
        # Check visited
        if v not in visited:
            visited.add(v)
            print(f"added v to visted: {visited}")
        # Check neighbors and...
            if v in neighbors:
                print("HERE")
                # iterate or...
                for neighbor in neighbors[v]:
                    print(f"neighbor: {neighbor}")
                    curr_path_copy = curr_path.copy()
                    curr_path_copy.append(neighbor)
                    paths.append(curr_path_copy)
                    print(f"paths: {paths}\n")
        else:
            break



"""
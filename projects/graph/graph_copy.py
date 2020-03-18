"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertext does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")        
        print(f"\n")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create a queue
        q = Queue()
        # Enque the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Deque the first vertex
            v = q.dequeue()        
            # Check if it has been visited            
            # If it hasnt been visited....
            if not v in visited:
                # Mark it as visited
                print(f"has not been visited: {v} (bft)")
                visited.add(v)
                # Enqueue all it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
        print(visited)
        print(f"\n")
        


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it has been visited
            # If it hasnt been visited...
            if not v in visited:
                # Mark it as visited
                print(f"has not been visited: {v} (dft)")
                visited.add(v)
                # Push all it's neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)
        print(visited)
        print(f"\n")

    def dft_recursive(self, starting_vertex, visited= set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print("DFT RECURSIVE \n")
        # TODO
        # Check if the node has been visited
        
        if starting_vertex is None:
            return
        
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            print(visited)
            print(f"neighbor: {self.get_neighbors(starting_vertex)}")        

            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        else:
            return
        # If not...
            # Mark it as visited
            # Call dft_recursive on each neighbor
        """ 
            "the tricky thing aobut this is that you are going to have to figure out how to
            carry over the visited array to all of the recursive calls." 
            A: you can do a nested function or you can set a default arg
         """


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.      

        """    
        # TODO
        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        print("==========START==========")     
        print(f"q.enqueue = {q.queue}\n")
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            first_path = q.dequeue()
            print(f"first_path: {first_path}")          
                  
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = first_path[-1]   
            print(f"end vertex, v = {v}\n")
            # Check if it's been visited ...            
            # If it hasn't been visited...
            if not v in visited:
                # Mark it as visited                
                visited.add(v)
                print(f"visited: {visited}")
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO RETURN THE PATH
                    return f"here's your path: {first_path}"
                # Enqueue a PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
                print(f"FOR LOOP")
                print(f"neighbors of {v}: {self.get_neighbors(v)}")
                for neighbor in self.get_neighbors(v):
                    first_path_copy = first_path.copy()
                    print(f"first_path_copy = {first_path_copy}")
                    first_path_copy.append(neighbor)                    
                    print(f"first_path_copy.enqueue(neighbor) = {first_path_copy}")
                    print(f"q = {q.queue}")
                    q.enqueue(first_path_copy)
                    print(f"q.enqueue(fist_paty_copy) = {q.queue}")
                print("\n")


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        # TODO
        # Create a queue
        s = Stack()
        # Enqueue A PATH TO the starting vertex
        s.push([starting_vertex])
        print("==========START==========")     
        print(f"q.enqueue = {s.stack}\n")
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while s.size() > 0:
            # Dequeue the first PATH
            first_path = s.pop()
            print(f"first_path: {first_path}")          
                  
            # GRAB THE VERTEX FROM THE END OF THE PATH
            v = first_path[-1]   
            print(f"end vertex, v = {v}\n")
            # Check if it's been visited ...            
            # If it hasn't been visited...
            if not v in visited:
                # Mark it as visited                
                visited.add(v)
                print(f"visited: {visited}")
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO RETURN THE PATH
                    return f"here's your path: {first_path}"
                # Enqueue a PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    # ENQUEUE THE COPY
                print(f"FOR LOOP")
                print(f"neighbors of {v}: {self.get_neighbors(v)}")
                for neighbor in self.get_neighbors(v):
                    first_path_copy = first_path.copy()
                    print(f"first_path_copy = {first_path_copy}")
                    first_path_copy.append(neighbor)                    
                    print(f"first_path_copy.enqueue(neighbor) = {first_path_copy}")
                    print(f"q = {s.stack}")
                    s.push(first_path_copy)
                    print(f"q.enqueue(fist_paty_copy) = {s.stack}")
                print("\n")
        

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)

        if starting_vertex == destination_vertex:
            return path_copy
        

        for neighbor in self.get_neighbors(starting_vertex):
            self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
        

        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    print(f"\n")
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    #graph.bft(1)

    

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)
    #graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print("\n")
    #print(graph.dfs_recursive(1, 6))

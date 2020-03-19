import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        possbible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possbible_friendships.append((user_id, friend_id))
        
        random.shuffle(possbible_friendships)

        # Create n friendships wher n = avg_friendships * num_users // 2
        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendship * num_users

        for i in range(num_users * avg_friendships // 2):
            friendship = possbible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        friendships = {1: {5}, 2: {8, 9}, 3: {9, 5}, 4: {8, 9, 5}, 5: {1, 3, 4}, 6: {7}, 7: {10, 6}, 8: {2, 4}, 9: {2, 3, 4}, 10: {7}}
        print(f"test_friendships: {friendships}\n")
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        for friendship in friendships:
            print(f"START search. path from id: {user_id} to user: {friendship}")            
            path = self.find_path(user_id, friendship, friendships) #temporarily pass friendship
            visited[friendship] = path
            
        
        
        return visited

    def find_path(self, user_id, destination_vertex, friendships):
        # Create a queue
        print(f"find_path({user_id}, {destination_vertex}, friendships)")
        visited = set()
        q = [[user_id]]
        print(f"q: {q}")
        # Enqueue a PATH TO the starting vertex
        
        # Create a set to store visited verticies (above, but dict)
        # if destination_vertex > 5:
        #     destination_vertex = 5
        # While the queue is not empty...
        while len(q) > 0:
            print(f"\nWHILE LOOP")
            # Dequeue the first PATH
            first_path = q.pop(0)
            print(f"first_path = {first_path}")
            # Grab the vertex from the end of the path
            v = first_path[-1]
            print(f"new v = {v}")
            # Check if it has been visited and             
            # If it hasn't been visited...
            if v not in visited:                
                # Check if it's the TARGET
                visited.add(v)
                print(f"visited.add(v) = {visited}")
                if v == destination_vertex:
                    # if target then return path
                    print(f"v is target: {v}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")                   
                    print(f"visited: {visited}")
                    print(f"returning path: {first_path}\n")
                    return first_path
                # Enqueue a path to all it's neighbors
                    # Make a copy of the path
                    # Enqueue the copy
                print(f"loop of ---> friendships[{v}]: {friendships[v]}")
                for friendship in friendships[v]:                    
                    first_path_copy = first_path.copy()
                    print(f"first_path_copy: {first_path_copy}")                
                    first_path_copy.append(friendship)
                    print(f"first_path_copy.append({friendship})")
                    q.append(first_path_copy)
                    print(f"q.append(first_path_copy) =  {q}")
                    visited.add(v)
                    print(f"q: {q}")
                    print(f"visited: {visited} \n")
                

                
        

        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        
        """
        # TODO
        

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    #print(f"friendships: {sg.friendships}")
    connections = sg.get_all_social_paths(1)
    print(f"connections: {connections}")

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
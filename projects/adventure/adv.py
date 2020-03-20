from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

print(traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
room_dirs_to_explore = {}
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)

def update_rooms_to_explore(room_id, prev_room=None, prev_dir=None):
    print(f"\nupdate_rooms_to_explore({room_id})")
    room_dirs_to_explore[room_id] = {}  
    for direction in player.current_room.get_exits():  
        room_dirs = room_dirs_to_explore[room_id]
        room_dirs.update({direction: '?'})
        room_dirs_to_explore[room_id]['previous_direction'] = 'w'
    if prev_room is not None:
        room_dirs_to_explore[room_id][prev_dir] = prev_room
        room_dirs_to_explore[room_id]['previous_direction'] = prev_dir 
    print(f"{room_dirs_to_explore}\n")


print(f"====================START WHILE=================================")
#len(visited_rooms) != len(room_graph)  --> eventally test for this
count = 0
while True:
    print(f"len(visted_rooms):{len(visited_rooms)}, len(room_graph): {len(room_graph)}")
    if len(visited_rooms) == len(room_graph):
        break
    if count > 1000:
        break
    count += 1
    
    # ============ VARS =============
    #if player.current_room.id == 0:
    room_id = player.current_room.id # room id of the currnet room
    print(f"\nnow in room: {room_id}")
    if room_id not in room_dirs_to_explore:
        # save a key: dict pair to keep track of all the directions taken from a given room. use the function:
        update_rooms_to_explore(room_id)

    # write an algorithm that picks a random unexplored direction from the player's current room, travels, and logs that direction, then loops.
    # This should cuase your player to walk a depth-first traversal. whe yuu reach a dead-end ie. a room with no unexplored paths, walk back
    # to the nearest rooom that does not dontain an unexplored path. 

    possible_dirs = player.current_room.get_exits()
    explore_history = room_dirs_to_explore[room_id]    
    print(f"explore history: {explore_history}")

    unexplored_dirs = [direction for direction in explore_history if explore_history[direction] == '?']
    print(f"unexplored_dirs: {unexplored_dirs}")
    random_dir = None
    room_in_random_dir = None
    if len(unexplored_dirs):
        random_num = random.randrange(0, len(unexplored_dirs))
        random_dir = unexplored_dirs[random_num] 
        room_in_random_dir = player.current_room.get_room_in_direction(random_dir).id
    
    print(f"random_dir: {random_dir}")
    opposite = None
    if random_dir == 'n':
        opposite = 's'
    if random_dir == 's':
        opposite = 'n'
    if random_dir == 'e':
        opposite = 'w'
    if random_dir == 'w':
        opposite = 'e'

    if random_dir:        
        explore_history[random_dir] = room_in_random_dir # change form the room#: '?' to the room#: id of unexplored room.
        player.travel(random_dir)
        print(f"after player.travel({random_dir}), current_room = {player.current_room.id}")
        traversal_path.append(random_dir)        
        print(traversal_path)
        if room_id not in visited_rooms:
            visited_rooms.add(room_id)
            print(f"visited_rooms: {visited_rooms}")
        prev_dir = opposite
        prev_room = room_id
        # add current room to rooms_dirs_to_explore
        if player.current_room.id not in room_dirs_to_explore:
            update_rooms_to_explore(player.current_room.id, prev_room, prev_dir)
        else:
            room_dirs_to_explore[player.current_room.id][opposite] = room_id # this tracks room id from the direction player just came from
            room_dirs_to_explore[player.current_room.id]['previous_direction'] = opposite # log the previous direction for backtracking
    
    if len(unexplored_dirs) == 0:
        print(f"ZZZZZZZZZZZZZZZZZZZZZZZZZEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOOOOOOO")
        previous_direction = explore_history['previous_direction']
        player.travel(previous_direction)
        traversal_path.append(previous_direction)
    
print(f"==================WHILE FINISHED==========================")
print(f"traversal_path: {traversal_path}")
print(f"visited_roooms: {visited_rooms}")
print(f"count: {count}")
print(f"===========================================================\n")

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room.id)
    
if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

print(f"player.current_room: {player.current_room.id}")
print(f"visited_rooms: {visited_rooms}")









#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


#dft
# Create a stack --> taversal_path
# Push the starting --> list of directions
# Create a set to store visited rooms --> visited_rooms
# While the stack is not empty...
# while possible_paths is not empty:
#     # Pop the first --> list of directions
#     current_path = possible_paths.pop(0)
#     # Check current_room has been visited    
#     # If it hasn't been visited...
#         if player.current_room.id not in visited_rooms:
#         #Mark it as visited
#             visited_rooms.add(player.current_room.id)
#         #Push all of it's directions


# print(f"room {room_id}'s unexplored_dirs: {unexplored_dirs}")
#     if len(unexplored_dirs) > 0:
#         next_dir = unexplored_dirs.pop(0) # pop of the first direction 
#         room_in_next_dir = player.current_room.get_room_in_direction(next_dir).id # find the id of the room in the next direction      
#         print(f"next_dir: {next_dir}")
#         print(f"room_in_next_dir: {room_in_next_dir}")
#         # if the room in the next direction has not been visited...
#         if room_in_next_dir not in visited_rooms:
#             # add the room to visited rooms
#             visited_rooms.add(player.current_room.id)
#             # add the direction to the traversal path: i.e. n, s, e, w
#             traversal_path.append(next_dir)
#             # travel to the next room (room_in_next_dir becomes the current room)
#             player.travel(next_dir)

#         # if the room in next direction HAS been visited, but still has directions to explore...
#         elif room_in_next_dir in visited_rooms and len(room_dirs_to_explore[room_in_next_dir]) > 0:
#             # add the next direction to the traversal path
#             traversal_path.append(next_dir)
#             # travel to the next room
#             player.travel(next_dir)

#     print(f"room {room_id}'s' updated unexplored_dirs: {unexplored_dirs}")
#     print(f"room_dir_to_explore: {room_dirs_to_explore}\n")




# BFS:
# def bfs(neighbors, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.      

#         """    
#         # TODO
#         # Create a queue
#         q = []
#         # Enqueue A PATH TO the starting vertex
#         q.append([starting_vertex])
        
#         # Create a set to store visited vertices
#         visited = set()
#         # While the queue is not empty...
#         while q.size() > 0:
#             # Dequeue the first PATH
#             first_path = q.pop(0)                 
                  
#             # GRAB THE VERTEX FROM THE END OF THE PATH
#             v = first_path[-1]   
            
#             # Check if it's been visited ...            
#             # If it hasn't been visited...
#             if not v in visited:
#                 # Mark it as visited                
#                 visited.add(v)
                
#                 # CHECK IF IT'S THE TARGET
#                 if v == destination_vertex:
#                     # IF SO RETURN THE PATH
#                     return first_path
#                 # Enqueue a PATH TO all it's neighbors
#                     # MAKE A COPY OF THE PATH
#                     # ENQUEUE THE COPY
                
#                 for neighbor in neighbors:
#                     first_path_copy = first_path.copy()                    
#                     first_path_copy.append(neighbor)               
#                     q.enqueue(first_path_copy)
                    
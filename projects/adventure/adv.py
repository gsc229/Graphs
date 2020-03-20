from room import Room
from player import Player
from world import World
from bfs import bfs
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

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)
possible_exits = player.current_room.get_exits()
print(f"{possible_exits}")

travel_graph = {}

def update_travel_graph(room_id, prev_or_next_room=None, prev_or_next_dir=None):    
    # initiate a dictionary for a NEW room to take directions:
    if prev_or_next_room is None:
        travel_graph[room_id] = {}  
        for direction in player.current_room.get_exits():  
            room_dirs = travel_graph[room_id]
            room_dirs.update({direction: '?'})
        #print(f"\nadded new room to travel graph - update_travel_graph({room_id})")
    if prev_or_next_room is not None:
        travel_graph[room_id][prev_or_next_dir] = prev_or_next_room
        #print(f"\nupdating room info in update_travel_graph({room_id})")
        
    #print(f"{travel_graph}\n")

def get_unexplored_dir(room_id):
    all_directions = travel_graph[room_id]
    unexplored = [direction for direction in all_directions if all_directions[direction] == '?']
    ##print(f"unexplored: {unexplored}")
    
    if len(unexplored) == 0:
        return None
    else:
        random_num = random.randrange(0, len(unexplored))
        return unexplored[random_num]

def update_logs(room_id, direction):    
    #print(f"\nUpdating Logs!!!")
    # before swithcing to new room
    # update the traversal path for the current direction
    old_room = player.current_room
    room_in_next_direction = old_room.get_room_in_direction(direction).id
    #print(f"current_room: {old_room.id}, room_in_next_direction({direction}): {room_in_next_direction}")
    travel_graph[old_room.id][direction] = room_in_next_direction
    

    # find the opposite direction to updated direction of room coming from
    opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    player.travel(direction)
    traversal_path.append(direction)
    # player is now in a new room
    new_room = player.current_room
    # after travel, check to see if the new room has been logged in the graph
    if new_room.id not in travel_graph:
        # if it hasn't initiate a new dictionary in the graph, then immediately add the direction,
        # and room the player came from
        update_travel_graph(new_room.id)
        update_travel_graph(new_room.id, old_room.id, opposite[direction])

    # else if it has, update the direction with the room the player came from.
    else:
        update_travel_graph(new_room.id, old_room.id, opposite[direction])
    #print(f"\nLogs updated!!!")
    #print(f"traversal_path: {traversal_path}")
    #print(f"travel_graph: {travel_graph}\n")



# ================ WHILE LOOP =================================
count = 0
while len(travel_graph) < len(room_graph):
    count += 1
    if player.current_room.id not in travel_graph:
        update_travel_graph(player.current_room.id)

    unexplored_direction = get_unexplored_dir(player.current_room.id)
    #print(f"{unexplored_direction}")

    # WALK IN UNEXPLORED DIRECTION
    if unexplored_direction is not None:
        #print(f"now in room {player.current_room.id}")
        update_logs(player.current_room.id, unexplored_direction)

    # IF YOU REACH A DEAD END
    if unexplored_direction is None:
        direction_set = bfs(travel_graph, player.current_room.id, '?')
        print(f"direction_set: {direction_set}")
        setps_to_unexplored = direction_set[1]
        print(f"steps_to_unexplored: {setps_to_unexplored}")
        for step in setps_to_unexplored:
            print(f"STEP: {step}")
            player.travel(step)
            print(f"player.current_room: {player.current_room.id}")
        
        
    

print(f"====================END WHILE LOOP===========================================\n")
print(f"travel_graph: {travel_graph}\n")
print(f"traversal_path: {traversal_path}")
print(f"moves: {len(traversal_path)}")
print(f"\n====================END WHILE LOOP===========================================\n")

player.current_room = world.starting_room


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room.id)
    #print(visited_rooms)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


# do sth
        #print("NADA")
        # opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
        
        # reverse_travel_path = traversal_path.copy()
        # reverse_travel_path.reverse()
        # #print(f"original:     {traversal_path}")
        # #print(f"reverse_path: {reverse_travel_path}")
        
        # for direction in reverse_travel_path:
        #     #print(direction)
        #     player.travel(opposite[direction])
        #     traversal_path.append(opposite[direction])
            
        #     if get_unexplored_dir(player.current_room.id) is not None:
        #         break
        #     #print(f"player entered room: {entered_room.id}")
            
            
        #     # if entered_room.id not in travel_graph:
        #     #     update_travel_graph(entered_room.id)
                
        #     # #print(f"traversal_info of entered room: {travel_graph[player.current_room.id]}")
        #     # for direction in travel_graph[entered_room.id]:
        #     #     #print(direction)
        #     #     if travel_graph[entered_room.id][direction] == '?':
        #     #         new_direction = get_unexplored_dirs(entered_room.id)
        #     #         player.travel(new_direction)
        #     #         traversal_path.append(new_direction)
        # #print(f"traversal_path: {traversal_path}")
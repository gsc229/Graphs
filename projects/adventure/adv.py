from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
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
visited_rooms.add(player.current_room)
possible_exits = player.current_room.get_exits()
print(f"{possible_exits}")

travel_graph = {}

def update_travel_graph(room_id, prev_room=None, prev_dir=None):
    print(f"\nupdate_rooms_to_explore({room_id})")
    travel_graph[room_id] = {}  
    for direction in player.current_room.get_exits():  
        room_dirs = travel_graph[room_id]
        room_dirs.update({direction: '?'})
        
    if prev_room is not None:
        travel_graph[room_id][prev_dir] = prev_room
        
    print(f"{travel_graph}\n")

def get_unexplored_dirs(room_id):
    all_directions = travel_graph[room_id]
    unexplored = [direction for direction in all_directions if all_directions[direction] == '?']
    print(f"unexplored: {unexplored}")
    #unexplored_dirs = [direction for direction in explore_history if explore_history[direction] == '?']
    if len(unexplored) == 0:
        return None
    else:
        random_num = random.randrange(0, len(unexplored))
        return unexplored[random_num]

    

while len(visited_rooms) < len(room_graph):

    if player.current_room.id not in travel_graph:
        update_travel_graph(player.current_room.id)

    unexplored_direction = get_unexplored_dirs(player.current_room.id)
    print(f"{unexplored_direction}")

    if unexplored_direction is None:
        # do sth
        print("NADA")
    else:
        player.travel(unexplored_direction)
        print(f"now in room {player.current_room.id}")


    break


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

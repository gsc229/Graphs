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
traversal_path = ["n", "n", "s", "s", "s", "s", "n", "n", "e", "e", "w", "w", "w", "w"]



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room.id)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while len(traversal_path) >=0:
    print(f"len(visted_rooms): {len(visited_rooms)}, len(room_graph): {len(room_graph)}")
    if len(visited_rooms) == len(room_graph):
        print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
        break
    
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    #cmds = input("-> ").lower().split(" ")
    cmd = traversal_path.pop(0)
    print(f"cmd: {cmd}")
    if cmd in ["n", "s", "e", "w"]:
        player.travel(cmd, True)
        world.print_rooms()
        if player.current_room not in visited_rooms:
            visited_rooms.add(player.current_room.id)
            print(f"visited rooms: {visited_rooms}")
            print(f"current room: {player.current_room.description}")
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
print(f"visited rooms: {visited_rooms}")
from helpers import Map, load_map
from helper import Maps, load_maps
from student_code import shortest_path


map_10 = load_map('map-10.pickle')
#show_map(map_10)

map_40 = load_map('map-40.pickle')

path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)
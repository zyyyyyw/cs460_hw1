#create map from txt file for all the search algorithms

#load all the points from txt file


def load_map(file_path):
    map_file = open(file_path,'r')
    coordinates = map_file.read()
    map_file.close()
    world_boundary, obstacles, start_goal = coordinates.split('---')
    world_boundary = turn_to_list(world_boundary)
    obstacles = obstacles.strip().split("\n")
    obstacles = [turn_to_list(word) for word in obstacles]
    start_goal = start_goal.strip().split('\n')
    start_goal = [turn_to_list(word) for word in start_goal]
    return world_boundary,obstacles, start_goal


def turn_to_list(str):
    str_list = str.split()
    list = []
    for word in str_list:
        word = word[1:-1]
        x,y = word.split(',')
        list.append((float(x),float(y)))
    return list

#construct map for A*, give a list of coordiante for where the robot can't go


def black_list(world_bundary, obstacles):
    list = []
    x_range = [x for x,y in world_bundary]
    min_x = min(x_range)
    max_x = max(x_range)
    y_range = [y for x,y in world_bundary]
    min_y = min(y_range)
    max_y = max(y_range)
    #go through all the vertex on the map
    for x in range (int(min_x),int(max_x+1),1):
        for y in range(int(min_y), int(max_y+1), 1):
            if x < min_x+1 or x > max_x-1 or y > max_y-1 or y < min_y+1 or not check_obstacles(x,y,obstacles):
                list.append((x,y))
    return list


def check_obstacles(x,y,obstacles):
    for obstacle in obstacles:
        x_range = [x for x, y in obstacle]
        min_x = min(x_range)
        max_x = max(x_range)
        y_range = [y for x, y in obstacle]
        min_y = min(y_range)
        max_y = max(y_range)
        if x >= min_x or x <= max_x or y <= max_y or y >= min_y:
            return False
    return True




def process(num):
    if num>0:
        return num-1
    elif num<0:
        return num+1


world_boundary, obstacles, start_goal = load_map('/Users/segfault/Desktop/map_1.txt')
print black_list(world_boundary, obstacles)
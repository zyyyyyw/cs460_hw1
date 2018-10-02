# create map from txt file for all the search algorithms

# load all the points from txt file
import math

def load_map(file_path):
    map_file = open(file_path, 'r')
    coordinates = map_file.read()
    map_file.close()
    world_boundary, obstacles, start_goal = coordinates.split('---')
    world_boundary = turn_to_list(world_boundary)
    obstacles = obstacles.strip().split("\n")
    obstacles = [turn_to_list(word) for word in obstacles]
    start_goal = start_goal.strip().split('\n')
    start_goal = [turn_to_list(word) for word in start_goal]
    return world_boundary, obstacles, start_goal


def turn_to_list(str):
    str_list = str.split()
    list = []
    for word in str_list:
        word = word[1:-1]
        x, y = word.split(',')
        list.append((float(x), float(y)))
    return list


# construct map for A*, give a list of coordinate for where the robot can't go


def black_list(world_boundary, obstacles):
    list = []
    x_range = [x for x, y in world_boundary]
    min_x = min(x_range)
    max_x = max(x_range)
    y_range = [y for x, y in world_boundary]
    min_y = min(y_range)
    max_y = max(y_range)

    # add all the boundary to the list
    for x in range(int(min_x), int(max_x) + 1, 1):
        list.append((float(x), min_y))
        list.append((float(x), max_y))
    for y in range(int(min_y), int(max_y) + 1, 1):
        list.append((min_x, float(y)))
        list.append((max_x, float(y)))

    # check for obstacles
    for obstacle in obstacles:
        x_min, x_max, y_min, y_max = get_min_max(obstacle)
        # get range of x, y to judge if the point is inside or outside the obstacles
        # get all the functions from each edge
        # y = ax + b
        # which will be stored like (a, b)
        list_of_functions = []
        obstacle.append(obstacle[0])
        y_dict = {}
        x_dict = {}
        for index in range(0, len(obstacle) - 1, 1):
            obstacle1 = obstacle[index]
            obstacle2 = obstacle[index + 1]
            x1, y1 = obstacle1
            x2, y2 = obstacle2
            min_y12 = int(min(y1, y2))
            max_y12 = int(max(y1, y2))
            min_x12 = int(min(x1, x2))
            max_x12 = int(max(x1, x2))
            if x1 == x2:
                for x12_y in range(min_y12, max_y12 + 1, 1):
                    add_to_dict(x12_y, x1, y_dict)
                    e_coord_x = (float(x1),float(x12_y))
                    if e_coord_x not in list:
                        list.append(e_coord_x)
            elif y1 == y2:
                for y12_x in range(min_x12, max_x12 + 1, 1):
                    add_to_dict(y12_x, y1, x_dict)
                    e_coord_y = (float(y12_x), float(y1))
                    if e_coord_y not in list:
                        list.append(e_coord_y)
            else:
                list_of_functions.append(calculate_function(obstacle1, obstacle2))
        close_x_min, close_x_max, close_y_min, close_y_max = get_close_min_max(obstacle)
        for function in list_of_functions:
            for x_inter in range(close_x_min, close_x_max + 1, 1):
                add_to_dict(x_inter, get_intersect_x(function, x_inter), x_dict)
            for y_inter in range(close_y_min, close_y_max + 1, 1):
                add_to_dict(y_inter, get_intersect_y(function, y_inter), y_dict)
        for y_key in y_dict.keys():
            inter_list_x = y_dict[y_key]
            inter_list_x = sorted(inter_list_x)
            for x_bound in range(0,len(inter_list_x)-1, 2):
                for x_val in range(int(inter_list_x[x_bound]), int(inter_list_x[x_bound+1]), 1):
                    coord1 = (float(x_val),float(y_key))
                    if coord1 not in list:
                        list.append((coord1))
        for x_key in x_dict.keys():
            inter_list_y = x_dict[x_key]
            inter_list_y = sorted(inter_list_y)
            for y_bound in range(0,len(inter_list_y)-1, 2):
                for y_val in range(int(inter_list_y[y_bound]), int(inter_list_y[y_bound+1]), 1):
                    coord2 = (float(x_key), float(y_val))
                    if coord2 not in list:
                        list.append(coord2)
        inter_list = [coord for coord in obstacle]
        for x_key in x_dict.keys():
            for x_key_val in x_dict[x_key]:
                inter_coord_x = (float(x_key), float(x_key_val))
                if inter_coord_x not in inter_list:
                    inter_list.append(inter_coord_x)
        for y_key in y_dict.keys():
            for y_key_val in y_dict[y_key]:
                inter_coord_y = (float(y_key_val), float(y_key))
                if inter_coord_y not in inter_list:
                    inter_list.append(inter_coord_y)
        for outer_x in range(x_min, x_max+1, 1):
            for outer_y in range(y_min, y_max+1, 1):
                outer_coord = (float(outer_x),float(outer_y))
                if outer_coord not in list:
                    for inter_coord in inter_list:
                        if get_distance(outer_coord,inter_coord)<=0.25:
                            list.append(outer_coord)
    return list


def get_min_max(obstacle):
    x_range = [x for x, y in obstacle]
    y_range = [y for x, y in obstacle]
    x_min = min(x_range)
    x_max = max(x_range)
    if x_min % 1.0 != 0:
        x_min = float(int(x_min) - 1)
    if x_max % 1.0 != 0:
        x_max = float(int(x_max) + 1)
    y_min = min(y_range)
    y_max = max(y_range)
    if y_min % 1.0 != 0:
        y_min = float(int(y_min) - 1)
    if y_max % 1.0 != 0:
        y_max = float(int(y_max) + 1)
    return int(x_min), int(x_max), int(y_min), int(y_max)


def get_close_min_max(obstacle):
    x_range = [x for x, y in obstacle]
    y_range = [y for x, y in obstacle]
    x_min = min(x_range)
    x_max = max(x_range)
    if x_min % 1.0 != 0:
        x_min = float(int(x_min))
    if x_max % 1.0 != 0:
        x_max = float(int(x_max))
    y_min = min(y_range)
    y_max = max(y_range)
    if y_min % 1.0 != 0:
        y_min = float(int(y_min))
    if y_max % 1.0 != 0:
        y_max = float(int(y_max))
    return int(x_min), int(x_max), int(y_min), int(y_max)


def calculate_function(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    slop = (y2 - y1) / (x2 - x1)
    b = y1 - slop * x1
    return slop, b


def add_to_dict(key, val, dict):
    if key in dict.keys():
        dict[key].append(val)
    else:
        dict[key] = [val]


def get_intersect_x(function, x_inter):
    slop, b = function
    return slop*x_inter+b


def get_intersect_y(function, y_inter):
    slop, b = function
    return (y_inter-b)/slop


def get_distance(outer_coord, inter_coord):
    x1,y1 = outer_coord
    x2,y2 = inter_coord
    return math.sqrt(abs(x2-x1)**2+abs(y2-y1)**2)



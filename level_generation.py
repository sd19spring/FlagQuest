"""Generates playable level"""

import random

def place_colors(model):
    """ Instantiate Color_Actor objects for each color in the chosen flag """
    #MAY BE WRONG. COPY-PASTED FROM ANOTHER MODULE.
    model.color_objs = []
    for i in range(len(model.flag.colors)):
        x_cell = random.randint(0, model.grid_x_size-1)
        y_cell = random.randint(0, model.grid_y_size-1)
        coord = model.grid_cells[(x_cell,y_cell)].cell_coord
        model.color_objs.append(Color_Actor(model.flag.colors[i], model, coord[0], coord[1]))
        model.grid_cells[(x_cell,y_cell)].occupied = True
        model.grid_cells[(x_cell,y_cell)].type = 'color'

def get_open_squares(model):
    poss_directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1,1), (-1,1), (1,-1), (-1,-1)]
    for direction in poss_directions:
        model.grid_cells[model.player.grid_cell]

def get_valid_path(model, curr_pos, end_pos):
    """Uses [[blah]] pathfinding algorithm to generate a playable but randomized path"""

    # if no path: return None
    pass

def place_obstacles(model):
    """ Generate obstacles in the grid """
    #MAY BE WRONG. COPY-PASTED FROM ANOTHER MODULE.
    obstacle_types = {'mountain':(128, 128, 128),'mushroom':(200, 0, 0),'shrub':(0, 128, 0),'tree':(163, 105, 17)}    # these types distinguish which obstacles are affected by which flag stripes
    selected_obstacles = list(obstacle_types)[0:len(model.flag.colors)]    # limits number of obstacle type options to the number of Flag colors
    for i in range(10):     # 10 is arbitrary, we should replace with intentional number later
        x_cell = random.randint(0, model.grid_x_size-1)        # randomizes location of obstacle
        y_cell = random.randint(0, model.grid_y_size-1)
        coord = model.grid_cells[(x_cell,y_cell)].cell_coord
        type = random.choice(selected_obstacles)            # randomly chooses this obstacle's type
        color = obstacle_types[type]                        # finds the color associated with this obstacle's type
        model.obstacles.append(Obstacle((model.cell_size,model.cell_size),coord,type,color)) # change this to sprite Group later

        model.grid_cells[(x_cell,y_cell)].occupied = True
        model.grid_cells[(x_cell,y_cell)].type = 'obstacle'

def generate_level(model):

    while retry:
    curr_pos = model.player.position_c
    place_colors(model)
    path_order = random.shuffle(model.color_objs)
    ind = 0
    for color_obj in path_order:
        path = get_valid_path(model, curr_pos, color_obj.position)
        if not path:
            break
        place_colors(model)
        curr_pos = color_obj.positions

    #check if final segment is playable
    if get_valid_path:
        retry = False

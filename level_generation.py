"""Generates playable level"""

import random

class Frontier:
    """Outwardly expanding edge of flood fill for search algorithm"""
    def __init__(self, start, model):
        """Start is a cell, members are cells in frontier"""
        self.members = [start]
        self.current = start
        self.grid_dict = model.grid_cells

    def put(self, cell):
        self.members.append(cell)

    def get_all_member_coords(self):
        all_coords = []
        for member in self.members:
            all_coords.append(member.label)
        return all_coords

    def neighbors(self, cell):
        """Finds all valid neighbors (cell objects) of given cell"""
        next_list = []
        coord_list = []   #not currently used. For testing purposes
        #poss_directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1,0), (-1,-1), (0,-1), (1,-1)]
        poss_directions = [(1, 0), (0, 1), (-1,0), (0,-1)]
        for direction in poss_directions:
            coord = (cell.label[0] + direction[0],
                        cell.label[1] + direction[1])
            if coord in self.grid_dict and coord not in self.get_all_member_coords() and not self.grid_dict[coord].occupied:
                next_list.append(self.grid_dict[coord])
                coord_list.append(coord)
        return next_list


def get_valid_path(model, start_cell, end_cell):
    """Uses simple breadth-first pathfinding algorithm to generate path from one
    cell to another.
    Based on https://www.redblobgames.com/pathfinding/a-star/introduction.html
    Includes start cell but not end cell."""


    # sweep through all coordinates to get all paths to start
    frontier = Frontier(start_cell, model)
    came_from = {}
    came_from[start_cell] = None

    while end_cell not in frontier.members:     #goes until hits end cell
        current = frontier.members[0]
        for next in frontier.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
        del frontier.members[0]

    # trace back through sweep to find path
    current_check = end_cell
    path = []
    path_coords = []  #Not currently in use. For debugging purposes
    while current_check != start_cell:
       path.append(current_check)
       current_check = came_from[current_check]
       path_coords.append(current_check.label)

    path.reverse()
    path_coords.reverse()

    return path

def get_zigzag_path(model, start_cell, end_cell, num_stops):
    """Returns valid path with specified number of random stops along the way
    Includes start and end cells. (but if that turned out to be bad later, easy
    to change. Remove end cell here, remove start cell in get_valid_path)"""

    cells = [start_cell]
    for stop in list(range(num_stops)):
        random_coord = (random.randint(1,45),random.randint(1,22))
        cells.append(model.grid_cells[random_coord])
    cells.append(end_cell)

    path = []
    for i in list(range(num_stops+1)):
        segment = get_valid_path(model, cells[i], cells[i+1])
        path.append(segment)
    path.append(end_cell)

    return path

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


def place_obstacles(model):
    """ Generate obstacles in the grid """
    #MAY BE WRONG. COPY-PASTED FROM ANOTHER MODULE.
    #TODO: place lines of objects so as to have barriers.
    #Also, place more so as to be more challenging. (Lauren)

    # for cells within three of current cell
    # if cell is not occupied
    # if type is not path
    # if random number is greater that 0.5
    # create an object on that cell 
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
            if path:
                retry = False
            place_colors(model)
            curr_pos = color_obj.positions

        #check if final segment is playable
        if get_valid_path:
            retry = False

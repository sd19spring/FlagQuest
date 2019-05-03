"""Generates playable level"""

import random



class Frontier:
    """Outwardly expanding edge of flood fill for search algorithm"""
    def __init__(self, start, grid_cells):
        """Start is a cell, members are cells in frontier"""
        self.members = [start]
        self.current = start
        self.grid_dict = grid_cells

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
            if (coord in self.grid_dict and coord not in self.get_all_member_coords()):
                next_list.append(self.grid_dict[coord])
                coord_list.append(coord)
        return next_list


def get_valid_path(grid_cells, start_cell, end_cell):
    """Uses simple breadth-first pathfinding algorithm to generate path from one
    cell to another.
    Based on https://www.redblobgames.com/pathfinding/a-star/introduction.html
    Includes start cell but not end cell."""

    # sweep through all coordinates to get all paths to start
    frontier = Frontier(start_cell, grid_cells)
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
       current_check.type = 'path'
       path.append(current_check)
       current_check = came_from[current_check]
       path_coords.append(current_check.label)

    path.reverse()
    path_coords.reverse()

    return path

def get_zigzag_path(grid_cells, start_cell, end_cell, num_stops):
    """Returns valid path with specified number of random stops along the way
    Includes start and end cells. (but if that turned out to be bad later, easy
    to change. Remove end cell here, remove start cell in get_valid_path)"""

    cells = [start_cell]
    for stop in list(range(num_stops)):
        random_cell = get_random_cell(grid_cells)
        cells.append(random_cell)
    cells.append(end_cell)

    path = []
    for i in list(range(num_stops + 1)):
        segment = get_valid_path(grid_cells, cells[i], cells[i+1])
        path.extend(segment)
    path.append(end_cell)

    return path

def get_random_cell(grid_cells):
    random_coord = (random.randint(1,45),random.randint(1,22))
    if not grid_cells[random_coord].occupied:
        return grid_cells[random_coord]
    else:
        return get_random_cell(grid_cells)

def place_colors(model):
    """ Instantiate Color_Actor objects for each color in the chosen flag """
    #MAY BE WRONG. COPY-PASTED FROM ANOTHER MODULE.

    model.color_objs = []
    for i in list(range(len(model.flag.colors))):
        x_cell = random.randint(0, model.grid_x_size-1)
        y_cell = random.randint(0, model.grid_y_size-1)
        coord = model.grid_cells[(x_cell,y_cell)].cell_coord
        model.color_objs.append(Color_Actor(model.flag.colors[i], model, coord[0], coord[1]))
        model.grid_cells[(x_cell,y_cell)].occupied = True
        model.grid_cells[(x_cell,y_cell)].type = 'color'


def place_obstacles(path, ind):
    """ Generate obstacles in the grid """
    #MAY BE WRONG. COPY-PASTED FROM ANOTHER MODULE.
    #TODO: place lines of objects so as to have barriers.
    #Also, place more so as to be more challenging. (Lauren)
    self.obstacles = []
    self.cleared_obstacles = []

    obstacle_types = self.flag.colors[:ind+1]

    for i in range(50):
        x_cell = random.randint(0, self.grid_size[0]-1)
        y_cell = random.randint(0, self.grid_zie[1]-1)
        while self.grid_cells[(x_cell, y_cell)].type == 'obstacle' or self.grid_cells[(x_cell, y_cell)].type == 'path':
            x_cell = random.randint(0, self.grid_size[0]-1)
            y_cell = random.randint(0, self.grid_zie[1]-1)

        coord = self.grid_cells[(x_cell,y_cell)].cell_coord
        type = random.choice(obstacle_types)            # randomly chooses this obstacle's type
        obstacle = actors.Obstacle((self.cell_size),coord,type)

        obstacle.make_groups(obstacle, self.obstacles)    # add obstacle to group based on what the obstacle's type is

        self.grid_cells[(x_cell,y_cell)].occupied = True
        self.grid_cells[(x_cell,y_cell)].type = 'obstacle'


    # for step in path:
    #     for direc in directions:
    #         curr_cell = model.grid_cells[(step.grid_coord[0] + direc[0], step.grid_coord[1] + direc[1])]
    #         if not curr_cell.occupied:
    #             if not curr_cell.type == 'path':
    #                 if random.random() >= 0.5:
    #                     coord = curr_cell.cell_coord
    #                     type = random.choice(selected_obstacles)            # randomly chooses this obstacle's type
    #                     color = obstacle_types[type]                        # finds the color associated with this obstacle's type
    #                     model.obstacles.append(Obstacle((model.cell_size,model.cell_size),coord,type,color)) # change this to sprite Group later
    #
    #                     model.grid_cells[(x_cell,y_cell)].occupied = True
    #                     model.grid_cells[(x_cell,y_cell)].type = 'obstacle'
    #     if not color_num == 1:
    #         if random.random() >= 0.5:
    #             coord = curr_cell.cell_coord
    #             type = random.randint(1,color_num)         # randomly chooses this obstacle's type
    #             color = obstacle_types[type]                        # finds the color associated with this obstacle's type
    #             model.obstacles.append(Obstacle((model.cell_size,model.cell_size),coord,type,color)) # change this to sprite Group later
    #
    #             model.grid_cells[(x_cell,y_cell)].occupied = True
    #             model.grid_cells[(x_cell,y_cell)].type = 'obstacle'
    #
    #     self.obstacles = []              # instantiates a list of all obstacle sprite groups
    #     self.cleared_obstacles = []
    #
    #     obstacle_types = self.flag.colors      # makes list of possible obstacle types based off of the flag's colors
    #
    #     for i in range(200):     # 10 is arbitrary, we should replace with intentional number later
    #         x_cell = random.randint(0, self.grid_size[0]-1)        # randomizes location of obstacle
    #         y_cell = random.randint(0, self.grid_size[1]-1)
    #         while self.grid_cells[(x_cell, y_cell)].occupied == True:   # re-randomizes location if the location is occupied by a color_obj
    #             x_cell = random.randint(0, self.grid_size[0]-1)
    #             y_cell = random.randint(0, self.grid_size[1]-1)
    #
    #         coord = self.grid_cells[(x_cell,y_cell)].cell_coord
    #         type = random.choice(obstacle_types)            # randomly chooses this obstacle's type
    #         obstacle = actors.Obstacle((self.cell_size),coord,type)
    #
    #         obstacle.make_groups(obstacle, self.obstacles)    # add obstacle to group based on what the obstacle's type is
    #
    #         self.grid_cells[(x_cell,y_cell)].occupied = True
    #         self.grid_cells[(x_cell,y_cell)].type = 'obstacle'

def generate_level(model):
    """Places"""
    end_cell = get_random_cell(model)
    while retry:
        curr_pos = model.player.position_c
        place_color(model)
        path_order = random.shuffle(model.color_objs)
        for color_obj in path_order:
            path = get_zigzag_path(model, curr_pos, color_obj.position)

            #NOT SURE IF THIS WILL WORK -- BREAKING CORRECT LOOP. COULD BE SOURCE OF PROBLEM
            if not path:
                break
            place_obstacles(model, path)
            place_color(model)
            curr_pos = color_obj.position

        retry = False

class Test_Model():
    def __init__(self, cell_size=40, grid_size=(46,23)):
        self.cell_size = cell_size
        self.grid_size = grid_size
        self.model = self.make_model()
        self.path = self.make_path()

    def make_model(self):
        """" Instantiate grid cells for game map """
        self.grid_cells = {}
        cell_size = (self.cell_size,self.cell_size)
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                cell_coord = (i*self.cell_size, 160+j*self.cell_size)
                self.grid_cells[(i,j)] = Cell(cell_coord, (i, j), False, 'none')


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

class Test_View():
    def __init__(self, model, screen_size=(1880,1080), fill=(0,0,0)):
        self.screen = pygame.display.set_mode(screen_size)
        self.fill = fill
        self.model = model

    def draw(self):
        """Draw the obstacles on the display"""
        for group in self.model.obstacles:       # places image of obstacle for each obstacle created in Model
            group.draw(self.screen)

        for step in self.model.path:
            pygame.draw.rect(self.screen,
                             (255,255,255),
                             pygame.Rect(step.cell_coord, self.model.cell_size, self.model.cell_size))

if __name__ == "__main__":
    model = Test_Model()
    view = Test_View(model)

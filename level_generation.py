"""This file holds the functions and classes for path planning when generating a playable level"""

import random

class Frontier:
    """Outwardly expanding edge of flood fill for search algorithm"""
    def __init__(self, start, grid_cells):
        """Start is a cell, members are cells in frontier"""
        self.members = [start]
        self.current = start
        self.grid_dict = grid_cells

    def put(self, cell):
        """ cell = Cell object to put in the list of members """
        self.members.append(cell)

    def get_all_member_coords(self):
        """ Returns a list of the coordinates of all member cells """
        all_coords = []
        for member in self.members:
            all_coords.append(member.label)
        return all_coords

    def neighbors(self, cell):
        """Finds all valid neighbors of given cell. Returns a list of Cell objects """
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
    """ Returns a random unoccupied Cell object from the grid """
    random_coord = (random.randint(1,45),random.randint(1,19))
    if not grid_cells[random_coord].occupied:
        return grid_cells[random_coord]
    else:
        return get_random_cell(grid_cells)

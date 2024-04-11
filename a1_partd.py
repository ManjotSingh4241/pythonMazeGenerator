from a3_maze import Maze

def find_path(maze, from_cell, to_cell):
    if from_cell == to_cell:
        return [from_cell]

    maze.mark_cell(from_cell)

    def is_cell_marked(neighbour):
        return not maze.get_is_marked(neighbour)

    def get_area(neighbour):
        if neighbour == to_cell:
            return [from_cell, neighbour]

    right_cell = maze.get_right(from_cell)
    if right_cell != -1 and is_cell_marked(right_cell):
        get_area(right_cell)
        path = find_path(maze, right_cell, to_cell)
        if path:
            path = [from_cell] + path
            return path

    left_cell = maze.get_left(from_cell)
    if left_cell != -1 and is_cell_marked(left_cell):
        get_area(left_cell)
        path = find_path(maze, left_cell, to_cell)
        if path:
            path = [from_cell] + path
            return path

    up_cell = maze.get_up(from_cell)
    if up_cell != -1 and is_cell_marked(up_cell):
        get_area(up_cell)
        path = find_path(maze, up_cell, to_cell)
        if path:
            path = [from_cell] + path
            return path

    down_cell = maze.get_down(from_cell)
    if down_cell != -1 and is_cell_marked(down_cell):
        get_area(down_cell)
        path = find_path(maze, down_cell, to_cell)
        
        if path:
            path = [from_cell] + path
            return path

    return []

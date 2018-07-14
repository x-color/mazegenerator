import random
import itertools


def generate1(maze):
    """
    穴掘り法
    """
    maze.fill_by_wall()
    maze.fill_edge_by_floor()
    start_positions = [(random.randrange(1, maze.width, 2),
                        random.randrange(1, maze.height, 2))]
    while len(start_positions) > 0:
        x, y = start_positions.pop()
        while True:
            maze.set_floor(x, y)
            x, y = _dig_to_next(maze, x, y)
            if x is None:
                break
            start_positions.append((x, y))
        random.shuffle(start_positions)
    maze.fill_edge_by_wall()


def _dig_to_next(maze, x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dir_x, dir_y in random.sample(directions, len(directions)):
        next_x, next_y = x + dir_x, y + dir_y
        next2_x, next2_y = next_x + dir_x, next_y + dir_y
        if maze.is_wall(next_x, next_y) and maze.is_wall(next2_x, next2_y):
            maze.set_floor(next_x, next_y)
            return next2_x, next2_y
    return None, None


def generate2(maze):
    """
    壁伸ばし法
    """
    maze.fill_by_floor()
    maze.fill_edge_by_wall()
    start_positions = list(itertools.product(range(2, maze.width - 2, 2),
                                            range(2, maze.height - 2, 2)))
    random.shuffle(start_positions)
    for x, y in start_positions:
        current_wall = []
        while maze.is_floor(x, y):
            maze.set_wall(x, y)
            current_wall.append((x, y))
            x, y = _extend_to_next(maze, x, y, current_wall)
            if x is None:
                break


def _extend_to_next(maze, x, y, current_wall):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dir_x, dir_y in random.sample(directions, len(directions)):
        next_x, next_y = x + dir_x, y + dir_y
        next2_x, next2_y = next_x + dir_x, next_y + dir_y
        if (next2_x, next2_y) not in current_wall:
            maze.set_wall(next_x, next_y)
            return next2_x, next2_y
    return None, None


def generate3(maze):
    """
    棒倒し法
    """
    maze.fill_by_floor()
    maze.fill_edge_by_wall()
    start_positions = list(itertools.product(range(2, maze.width - 2, 2),
                                            range(2, maze.height - 2, 2)))
    for x, y in start_positions:
        maze.set_wall(x, y)
        _lay_next(maze, x, y)


def _lay_next(maze, x, y):
    directions = [(0, -1), (1, 0), (-1, 0)]
    for dir_x, dir_y in random.sample(directions, len(directions)):
        next_x, next_y = x + dir_x, y + dir_y
        if maze.is_floor(next_x, next_y):
            maze.set_wall(next_x, next_y)
            return

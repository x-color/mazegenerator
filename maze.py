from textcolor import TextColor as Tc


class Maze:

    FLOOR = 0
    WALL = 1

    def __init__(self, width=5, height=5):
        assert width >= 5 and width % 2 == 1, \
            'Width must be odd number and more than 5'
        assert height >= 5 and height % 2 == 1, \
            'Height must be odd number and more than 5'
        self.width = width
        self.height = height
        self.fill_by_wall()

    def is_wall(self, x, y):
        return self.board[y][x] == Maze.WALL

    def is_floor(self, x, y):
        return self.board[y][x] == Maze.FLOOR

    def set_wall(self, x, y):
        self.board[y][x] = Maze.WALL

    def set_floor(self, x, y):
        self.board[y][x] = Maze.FLOOR

    def fill_by_wall(self):
        self.board = [[Maze.WALL for i in range(self.width)] for j in range(self.height)]

    def fill_by_floor(self):
        self.board = [[Maze.FLOOR for i in range(self.width)] for j in range(self.height)]

    def fill_edge_by_wall(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.set_wall(x, y)

    def fill_edge_by_floor(self):
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.set_floor(x, y)

    def display(self):
        board = ''
        for col in self.board:
            for position in col:
                if position == Maze.FLOOR:
                    board += Tc.white('  ', backgroud=True)
                else:
                    board += Tc.black('  ', backgroud=True)
            board += '\n'
        print(board)

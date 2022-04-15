import random
import time
class Snake:
    # __init__ is the constructor for a class.
    # The self parameter refers to the instance of the object.
    # Define the function __init__
    def __init__(self, maze):
        # the size of the maze
        self.maze = maze
        # the scores of the snakegame
        self.score = 0
        # food Coordinates
        self.food = [-1, -1]
        # Body of snake
        self.body = []
        # Board;告示牌
        self.board = [[False for col in range(maze)] for row in range(maze)]
        # path_board;路径告示牌
        self.path_board = [[False for col in range(maze)] for row in range(maze)]
        # Path;路径
        self.path = [[0 for col in range(maze)] for row in range(maze)]
        # Initialize the board;初始化告示牌
        self.init_board(self.board)
        # Initialize the snake body;初始化蛇身
        # Add coordinates to the existing body list.
        self.body.append([1,0])
        self.body.append([0,0])
        # Update the board;告示牌更新
        self.board[0][0] = True
        self.board[1][0] = True
        # Initialize the path matrix;初始化路径矩阵
        self.init_board(self.path_board)
        # Initialize the path vector;初始化路径向量
        self.init_path()
        # update path_board;更新path_board
        self.set_path_board([0, 0], True)
        # Create food command
        self.create_food()

    # Define the function init_board
    # Path matrix Setting as blank
    def init_board(self, tmp):
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                tmp[i][j] = False

    # Define the function is_not_all_true
    # Determine if there is a path, if it is not all True, then exists
    def is_not_all_true(self, tmp):
        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                if tmp[i][j] == False:
                    return True
        return False

    # Define the function create_food
    def create_food(self):
        # randint_Return a random integer N such that 0 <= N <= maze-1.
        self.food[0] = random.randint(0, self.maze-1)
        self.food[1] = random.randint(0, self.maze-1)
        # check if the food will create on the snake, if so, then recreate.
        while self.board[self.food[0]][self.food[1]]:
            self.food[0] = random.randint(0, self.maze-1)
            self.food[1] = random.randint(0, self.maze-1)
        ## can add or not
        self.del_path()
        self.form_path()

    # Define the function set_board_true
    # Set to True for given coordinates
    def set_board_true(self, coord):
        self.board[coord[0]][coord[1]] = True

    # Define the function set_board_false
    # Set the given coordinates to False
    def set_board_false(self, coord):
        self.board[coord[0]][coord[1]] = False

    # Define the function move_to
    # Pass in the coordinates of the next move, the snake moves
    def move_to(self, coord):
        # Determine if the next coordinate is a food coordinate
        if coord[0] != self.food[0] or coord[1] != self.food[1]:
            # next coordinate is not food
            # Clear snake tail position, set False
            self.set_board_false([self.body[-1][0],self.body[-1][1]])
            # Snake body list expel the snake tail
            # which means the overall length of the snake remains
            self.body.pop(-1)
            # Add a new snake head to the snake body list（move forward）
            self.body.insert(0, coord)
            # Add snake head coordinates, set True
            self.set_board_true(coord)
        else:
            # The next coordinate is food
            # Score plus one
            self.score += 1
            # Add a new snake head to the snake body list
            self.body.insert(0, coord)
            # Add snake head coordinates, set True
            self.set_board_true(coord)
            # create new food
            self.create_food()
        # delete the path where the food was last eaten
        self.del_path()
        # create new path
        self.form_path()

    # Create matrix
    # Define the function move
    # Snake moving direction
    def move(self):
        # console output dashboard
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                # food position
                if i == self.food[0] and j == self.food[1]:
                    print('#', end='')
                else:
                    if self.board[i][j]:
                        print('1', end='')
                    else:
                        print('0', end='')
            print('', end=' ')
            for k in range(len(self.path_board[i])):
                if self.path_board[i][k]:
                    print('1', end='')
                else:
                    print('0', end='')
            print('', end=' ')
            for l in range(len(self.path[i])):
                print(self.path[i][l], end='')
            print()
        print('-------------------------------')
        # Snake head
        tmp_point = self.body[0][:]
        # Determine the path direction of the snake head coordinates
        if self.path[self.body[0][0]][self.body[0][1]] == 0:
            # The direction is 0, then the next move coordinate x_coordinate minus one
            tmp_point[0] -= 1
            # snake move
            self.move_to(tmp_point)
        elif self.path[self.body[0][0]][self.body[0][1]] == 1:
            # The direction is 1, the next move coordinate x_coordinate plus one
            tmp_point[0] += 1
            # snake move
            self.move_to(tmp_point)
        elif self.path[self.body[0][0]][self.body[0][1]] == 2:
            # The direction is 2, the next move coordinate y_coordinate plus one
            tmp_point[1] += 1
            # snake move
            self.move_to(tmp_point)
        elif self.path[self.body[0][0]][self.body[0][1]] == 3:
            # The direction is 3, the next move coordinate y_coordinate minus one
            tmp_point[1] -= 1
            # snake move
            self.move_to(tmp_point)
        # Pause after move
        time.sleep(0.1)

    # Define the function init_path:
    # initialization the direction
    # 1 means the snake will turn right, 2 means the snake will turn down;
    # 0 means the snake will turn left, 3 means the snake will turn up.
    def init_path(self):
        for i in range(0, self.maze, 2):
            for j in range(0, self.maze, 2):
                self.path[i][j] = 1
                self.path[i + 1][j + 1] = 0
                self.path[i][j + 1] = 3
                self.path[i + 1][j] = 2
    # Define the function set_path_board
    # Set the orientation of the rectangle area
    def set_path_board(self, coord, bool):
        self.path_board[coord[0]][coord[1]] = bool
        self.path_board[coord[0]+1][coord[1]] = bool
        self.path_board[coord[0]][coord[1]+1] = bool
        self.path_board[coord[0]+1][coord[1]+1] = bool

    # Define the function matrix_no_point
    # Whether there is a snake body in the rectangular area
    def matrix_no_point(self, coord):
        return self.board[coord[0]][coord[1]] == False and self.board[coord[0]+1][coord[1]] == False and self.board[coord[0]][coord[1]+1] == False and self.board[coord[0]+1][coord[1]+1] == False

    # Define the function path_board_not_all_true
    # Determine if the path is not all True
    def path_board_not_all_true(self, coord):
        return not (self.path_board[coord[0]][coord[1]] and self.path_board[coord[0]+1][coord[1]+1])

    # Define the function add_path_matrix
    # Add rectangle area path
    def add_path_matrix(self, coord):
        if coord[0] % 2:
            if self.path_board_not_all_true(coord):
                self.path[coord[0]][coord[1]] = 1
                self.path[coord[0]+1][coord[1]+1] = 0
                self.set_path_board([coord[0]-1,coord[1]], True)
                self.set_path_board([coord[0]+1,coord[1]], True)
        else:
            if self.path_board_not_all_true(coord):
                self.path[coord[0]+1][coord[1]] = 2
                self.path[coord[0]][coord[1]+1] = 3
                self.set_path_board([coord[0],coord[1]+1], True)
                self.set_path_board([coord[0],coord[1]-1], True)

    # Define the function check_if_del
    # Check if the rectangle area path is deleted
    def check_if_del(self, coord):
        if self.board[coord[0]][coord[1]] == False and self.board[coord[0]+1][coord[1]] == False and self.board[coord[0]+1][coord[1]+1] == False and self.board[coord[0]][coord[1]+1] == False:
            self.set_path_board(coord, False)

    # Define the function del_path_matrix
    # delete rectangle area path
    def del_path_matrix(self, coord):
        if coord[0] % 2:
            self.path[coord[0]][coord[1]] = 2
            self.path[coord[0]+1][coord[1]+1] = 3
            self.check_if_del([coord[0]-1,coord[1]])
            self.check_if_del([coord[0]+1,coord[1]])
        else:
            self.path[coord[0]+1][coord[1]] = 0
            self.path[coord[0]][coord[1]+1] = 1
            self.check_if_del([coord[0],coord[1]-1])
            self.check_if_del([coord[0],coord[1]+1])

    # Define the function del_path
    # remove loop path and restore the original path board
    # the core of the algorithm
    def del_path(self):
        for i in range(0, self.maze, 2):
            for j in range(1, self.maze-2, 2):
                if self.matrix_no_point([i, j-1]) or self.matrix_no_point([i, j+1]):
                    self.del_path_matrix([i, j])
                if self.matrix_no_point([j-1, i]) or self.matrix_no_point([j+1, i]):
                    self.del_path_matrix([j, i])

    # Define the function form_path
    # add loop path
    # the core of the algorithm
    def form_path(self):
        headX = self.body[0][0]
        headY = self.body[0][1]
        # here the row and column coordinates of head and food are even
        # the even numbers are no larger than the original number
        headX = headX & 0xfffe
        headY = headY & 0xfffe
        endX = self.food[0]
        endY = self.food[1]
        endX = endX & 0xfffe
        endY = endY & 0xfffe
        dx = 0
        dy = 0
        if headX > endX:
            dx = -2
        else:
            dx = 2
        if headY > endY:
            dy = -2
        else:
            dy = 2
        while headX != endX:
            x = headX
            headX += dx
            self.add_path_matrix([(x+headX)//2, headY])
        while headY != endY:
            y = headY
            headY += dy
            self.add_path_matrix([endX, (headY+y)//2])
# test
if __name__ == "__main__":
    snake = Snake(4)
    while True:
        snake.move()
       # snake.add_path_matrix()
        #snake.create_food()


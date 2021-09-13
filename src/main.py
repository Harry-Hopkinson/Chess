import chess
import pygame
import time
import sys
from stockfish import stockfish
# pip install stockfish
# pip install chess

board = [[" " for i in range(8)] for i in range(8)]

class Piece:
    def __init__(self, team, type, image, canBeTaken=False):
        self.team = team
        self.type = type
        self.canBeTaken = canBeTaken
        self.image = image

# Black Pieces Imports
bp = Piece("b", "p", "Black_Pawn.png")
bb = Piece("b", "b", "Black_Bishop.png")
bk = Piece("b", "k", "Black_King.png")
bkn = Piece("b", "n", "Black_Knight.png")
bq = Piece("b", "q", "Black_Queen.png")
br = Piece("b", "r", "Black_Rook.png")

# White Pieces Import
wp = Piece("w", "p", "White_Pawn.png")
wb = Piece("w", "b", "White_Bishop.png")
wk = Piece("w", "k", "White_King.png")
wkn = Piece("w", "n", "White_Knight.png")
wq = Piece("w", "q", "White_Queen.png")
wr = Piece("w", "r", "White_Rook.png")

# Puts the Images in the Correct Order on the 8 by 8 Chess Board

starting_order = {(0, 0): pygame.image.load(br.image), (1, 0): pygame.image.load(bkn.image),
                  (2, 0): pygame.image.load(bb.image), (3, 0): pygame.image.load(bk.image),
                  (4, 0): pygame.image.load(bq.image), (5, 0): pygame.image.load(bb.image),
                  (6, 0): pygame.image.load(bkn.image), (7, 0): pygame.image.load(br.image),
                  (0, 1): pygame.image.load(bp.image), (1, 1): pygame.image.load(bp.image),
                  (2, 1): pygame.image.load(bp.image), (3, 1): pygame.image.load(bp.image),
                  (4, 1): pygame.image.load(bp.image), (5, 1): pygame.image.load(bp.image),
                  (6, 1): pygame.image.load(bp.image), (7, 1): pygame.image.load(bp.image),

                  (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None,
                  (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
                  (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None,
                  (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
                  (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None,
                  (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
                  (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None,
                  (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,

                  (0, 6): pygame.image.load(wp.image), (1, 6): pygame.image.load(wp.image),
                  (2, 6): pygame.image.load(wp.image), (3, 6): pygame.image.load(wp.image),
                  (4, 6): pygame.image.load(wp.image), (5, 6): pygame.image.load(wp.image),
                  (6, 6): pygame.image.load(wp.image), (7, 6): pygame.image.load(wp.image),
                  (0, 7): pygame.image.load(wr.image), (1, 7): pygame.image.load(wkn.image),
                  (2, 7): pygame.image.load(wb.image), (3, 7): pygame.image.load(wk.image),
                  (4, 7): pygame.image.load(wq.image), (5, 7): pygame.image.load(wb.image),
                  (6, 7): pygame.image.load(wkn.image), (7, 7): pygame.image.load(wr.image),}


def create_board(board):
    board[0] = [Piece('b', 'r', 'b_rook.png'), Piece('b', 'kn', 'b_knight.png'), Piece('b', 'b', 'b_bishop.png'), \
               Piece('b', 'q', 'b_queen.png'), Piece('b', 'k', 'b_king.png'), Piece('b', 'b', 'b_bishop.png'), \
               Piece('b', 'kn', 'b_knight.png'), Piece('b', 'r', 'b_rook.png')]

    board[7] = [Piece('w', 'r', 'w_rook.png'), Piece('w', 'kn', 'w_knight.png'), Piece('w', 'b', 'w_bishop.png'), \
               Piece('w', 'q', 'w_queen.png'), Piece('w', 'k', 'w_king.png'), Piece('w', 'b', 'w_bishop.png'), \
               Piece('w', 'kn', 'w_knight.png'), Piece('w', 'r', 'w_rook.png')]

    for i in range(8):
        board[1][i] = Piece('b', 'p', 'b_pawn.png')
        board[6][i] = Piece('w', 'p', 'w_pawn.png')
    return board

def on_board(position):
    if position[0] > -1 and position[1] -1 and position[0] <8 and position[1] < 8:
        return True

def convert_to_readable(board):
    output = ""

    for i in board:
        for j in i:
            try:
                output += j.team + j.type + ", "
            except:
                output += j + ", "
        output += "\n"
    return output

def deselect():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == "x ":
                board[row][column] = " "
            else:
                try:
                    board[row][column].canBeTaken
                except:
                    pass
    return convert_to_readeable(board)

################## Show Legal Moves ##################

def highlight(board):
    highlighted = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "x ":
                highlighted.append((i, j))
            else:
                try:
                    if board[i][j] == canBeTaken:
                        highlighted.append((i, j))
                except:
                    pass
                
    return highlighted

def check_team(moves, index):
    row, col = index
    if moves % 2 == 0:
        if board[row][col].team == "w":
            return True
    else:
        if board[row][col].team == "b":
            return True

def select_moves(piece, index, moves):
    if check_team(moves, index):
        if piece.type == "p":
            if piece.team == "b":
                return highlight(pawn_moves_b(index))
            else:
                return highlight(pawn_moves_w(index))

        if piece.type == "k":
            return highlight(king_moves(index))
        if piece.type == "r":
            return highlight(rook_moves(index))
        if piece.type == "b":
            return highlight(bishop_moves(index))
        if piece.type == "q":
            return highlight(queen_moves(index))
        if piece.type == "kn":
            return highlight(knight_moves(index))

################## Index Legal Moves ##################

def pawn_moves_b(index):
    if index[0] == 1:
        if board[index[0] + 2][index[1]] == '  ' and board[index[0] + 1][index[1]] == '  ':
            board[index[0] + 2][index[1]] = 'x '
    bottom3 = [[index[0] + 1, index[1] + i] for i in range(-1, 2)]

    for positions in bottom3:
        if on_board(positions):
            if bottom3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'b':
                        board[positions[0]][positions[1]].canBeTaken = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board

def pawn_moves_w(index):
    if index[0] == 6:
        if board[index[0] - 2][index[1]] == '  ' and board[index[0] - 1][index[1]] == '  ':
            board[index[0] - 2][index[1]] = 'x '
    top3 = [[index[0] - 1, index[1] + i] for i in range(-1, 2)]

    for positions in top3:
        if on_board(positions):
            if top3.index(positions) % 2 == 0:
                try:
                    if board[positions[0]][positions[1]].team != 'w':
                        board[positions[0]][positions[1]].canBeTaken = True
                except:
                    pass
            else:
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
    return board

##### Legal King Moves #####

def king_moves(index):
    for y in range(3):
        for x in range(3):
            if on_board((index[0] - 1 + y, index[1] - 1 + x)):
                if board[index[0] - 1 + y][index[1] - 1 + x] == " ":
                    board[index[0] - 1 + y][index[1] - 1 + x] = "x "
                else:
                    if board[index[0] - 1 + y][index[1] - 1 + x].team != board[index[0]][index[1]].team:
                        board[index[0] - 1 + y][index[1] - 1 + x].canBeTaken = True
    return board

##### Legal Rook Moves #####

def rook_moves(index):
    cross = [[[index[0] + i, index[1]] for i in range(1, 8 - index[0])],
             [[index[0] - i, index[1]] for i in range(1, index[0] + 1)],
             [[index[0], index[1] + i] for i in range(1, 8 - index[1])],
             [[index[0], index[1] - i] for i in range(1, index[1] + 1)]]

    for direction in cross:
        for positions in direction:
            if on_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].canBeTaken = True
                    break
    return board

##### Legal Bishop Moves #####

def bishop_moves(index):
    diagonals = [[[index[0] + i, index[1] + i] for i in range(1, 8)],
                 [[index[0] + i, index[1] - i] for i in range(1, 8)],
                 [[index[0] - i, index[1] + i] for i in range(1, 8)],
                 [[index[0] - i, index[1] - i] for i in range(1, 8)]]

    for direction in diagonals:
        for positions in direction:
            if on_board(positions):
                if board[positions[0]][positions[1]] == '  ':
                    board[positions[0]][positions[1]] = 'x '
                else:
                    if board[positions[0]][positions[1]].team != board[index[0]][index[1]].team:
                        board[positions[0]][positions[1]].canBeTaken = True
                    break
    return board

##### Legal Queen Moves #####


def queen_moves(index):
    board = rook_moves(index)
    board = bishop_moves(index)
    return board

##### Legal Knight Moves #####

def knight_moves(index):
    for i in range(-2, 3):
        for j in range(-2, 3):
            if i ** 2 + j ** 2 == 5:
                if on_board((index[0] + i, index[1] + j)):
                    if board[index[0] + i][index[1] + j] == '  ':
                        board[index[0] + i][index[1] + j] = 'x '
                    else:
                        if board[index[0] + i][index[1] + j].team != board[index[0]][index[1]].team:
                            board[index[0] + i][index[1] + j].canBeTaken = True
    return board

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Chess")

##### Hexadecimal Colours #####

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.occupied = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / 8, WIDTH / 8))

    def setup(self, WIN):
        if starting_order[(self.row, self.col)]:
            if starting_order[(self.row, self.col)] == None:
                pass
            else:
                WIN.blit(starting_order[(self.row, self.col)], (self.x, self.y))

def make_grid(rows, width):
    grid = []
    gap = WIDTH // rows
    print(gap)
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if (i+j) % 2 == 1:
                grid[i][j].colour = GREY
    return grid

def draw_grid(win, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j*gap, 0), (j * gap, width))


def update_display(win, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(win)
            spot.setup(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def Find_Node(pos, WIDTH):
    interval = WIDTH / 8
    y, x = pos
    rows = y // interval
    columns = x // interval
    return int(rows), int(columns)

def display_potential_moves(positions, grid):
    for i in positions:
        x, y = i
        grid[x][y].colour = BLUE


def Do_Move(OriginalPos, FinalPosition, WIN):
    starting_order[FinalPosition] = starting_order[OriginalPos]
    starting_order[OriginalPos] = None

def remove_highlight(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i+j) % 2 == 0:
                grid[i][j].colour = WHITE
            else:
                grid[i][j].colour = GREY

    return grid


            
    
            
        


stockfish = Stockfish("H:\Computer Science\Year 9\Chess\src\stockfish_engine\stockfish_14_x64_avx2")





############################### Stockfish Engine ###############################

# stockfish.get_board_visual() # A visual of the board will be printed - like the one below.

#+---+---+---+---+---+---+---+---+
#| r | n | b | q | k | b | n | r |
#+---+---+---+---+---+---+---+---+
#| p | p | p | p | p | p | p | p |
#+---+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+---+
#|   |   |   |   |   |   |   |   |
#+---+---+---+---+---+---+---+---+
#| P | P | P | P | P | P | P | P |
#+---+---+---+---+---+---+---+---+
#| R | N | B | Q | K | B | N | R |
#+---+---+---+---+---+---+---+---+

#stockfish.get_best_move()
#stockfish.set_position(["e2e4"])



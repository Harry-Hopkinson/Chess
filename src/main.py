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

# Returns Legal Moves

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



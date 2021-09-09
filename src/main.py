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




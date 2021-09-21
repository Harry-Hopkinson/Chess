############################### Install Stockfish ###############################

###### Windows ######
pip install stockfish

###### Ubuntu ######
sudo apt install stockfish

###### Mac Os ######
brew install stockfish


############################### Initialize Stockfish class ###############################
from stockfish import Stockfish
stockfish = Stockfish("/users/your path of stockfish on your computer")


############################### Set position by sequence of moves ###############################

###### By Certain Moves ######
stockfish.set_position(["e2e4", "e7e6"]) - # pawn has moved from e2 to e4 and black responds with pawn from e7 to e6 - the French Defense.
stockfish.make_moves_from_current_position(["g4d7", "a8b8", "f1d1"])

###### By FEN Notation ######
stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")


############################### Best Moves ###############################

###### Best Move ######
stockfish.get_best_move()

###### Get best move based on a time constraint ######
stockfish.get_best_move_time(1000) - # time in milliseconds - 1000 ms is one second.

###### Check is move correct with current position ######
stockfish.is_move_correct('a2a3') - # result is True or False

###### Get info on the top number of moves ######
stockfish.get_top_moves(n) - # set n to any number of the top moves you want to see - e.g three.
#{'Move': 'f5h7', 'Centipawn': None, 'Mate': 1},
#{'Move': 'f5d7', 'Centipawn': 713, 'Mate': None},
#{'Move': 'f5h5', 'Centipawn': -31, 'Mate': None}


############################### Engine Depth and Rating ###############################

###### Set current engines skill level (ignoring ELO rating) ######
stockfish.set_skill_level(15)

###### Set current engine's ELO rating (ignoring skill level) ######
stockfish.set_elo_rating(1350)

###### Set Stockfish Depth ######
stockfish.set_depth(15)

###### Get Engine's Parameters ######
stockfish.get_parameters()

{
    'Write Debug Log': 'false',
    'Contempt': 0,
    'Min Split Depth': 0,
    'Threads': 1,
    'Ponder': 'false',
    'Hash': 16,
    'MultiPV': 1,
    'Skill Level': 20,
    'Move Overhead': 30,
    'Minimum Thinking Time': 20,
    'Slow Mover': 80,
    'UCI_Chess960': 'false'
}


############################### Board and Visuals ###############################

###### Get current board position in Forsyth–Edwards notation (FEN) ######
stockfish.get_fen_position()
rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

###### Get current board visual ######
stockfish.get_board_visual()
+---+---+---+---+---+---+---+---+
| r | n | b | q | k | b | n | r |
+---+---+---+---+---+---+---+---+
| p | p | p | p | p | p | p | p |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
| P | P | P | P | P | P | P | P |
+---+---+---+---+---+---+---+---+
| R | N | B | Q | K | B | N | R |
+---+---+---+---+---+---+---+---+

###### Get current board evaluation in centipawns or mate in n ######
stockfish.get_evaluation()

{"type":"cp", "value":12}
{"type":"mate", "value":-3}
# Positive is advantage white, negative is advantage black #

###### Get current major version of stockfish engine ######
stockfish.get_stockfish_major_version() = 14












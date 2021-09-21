## Overview

Chess with Python using the Pygame Module and the Stockfish Engine.
[Stockfish](https://stockfishchess.org) is a free, powerful UCI chess engine
derived from Glaurung 2.1. Stockfish is not a complete chess program and requires a
UCI-compatible graphical user interface (GUI) (e.g. XBoard with PolyGlot, Scid,
Cute Chess, eboard, Arena, Sigma Chess, Shredder, Chess Partner or Fritz) in order
to be used comfortably. Read the documentation for your GUI of choice for information
about how to use Stockfish with it.

The Stockfish engine features two evaluation functions for chess, the classical
evaluation based on handcrafted terms, and the NNUE evaluation based on efficiently
updatable neural networks. The classical evaluation runs efficiently on almost all
CPU architectures, while the NNUE evaluation benefits from the vector
intrinsics available on most CPUs (sse2, avx2, neon, or similar).

## Files

This distribution of Stockfish consists of the following files:

  * [Readme.md](https://github.com/official-stockfish/Stockfish/blob/master/README.md), the file you are currently reading.

  * [Copying.txt](https://github.com/official-stockfish/Stockfish/blob/master/Copying.txt), a text file containing the GNU General Public License version 3.

  * [AUTHORS](https://github.com/official-stockfish/Stockfish/blob/master/AUTHORS), a text file with the list of authors for the project

  * [src](https://github.com/official-stockfish/Stockfish/tree/master/src), a subdirectory containing the full source code, including a Makefile
    that can be used to compile Stockfish on Unix-like systems.

  * a file with the .nnue extension, storing the neural network for the NNUE
    evaluation. Binary distributions will have this file embedded.
    
## Dependencies

This project needs the following commands to be installed. Use your command terminal for your native operating system.

pip intsall pygame - Windows
python3 -m pip install -U pygame --user - Mac Os


[![Build Status](https://github.com/official-stockfish/Stockfish/actions/workflows/stockfish.yml/badge.svg)](https://github.com/official-stockfish/Stockfish/actions)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/official-stockfish/Stockfish?branch=master&svg=true)](https://ci.appveyor.com/project/mcostalba/stockfish/branch/master)

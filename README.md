# Sudoku Solver
Solving Sudoku using the A* path finding algorithm.
## Installation
```sh
git clone https://github.com/adityaThakkar001/sudoku-solver.git
cd sudoku-solver
```
## Usage
1. Prepare your input file:
   Create a text file (e.g., sudoku_input.txt) containing the Sudoku puzzle. Use `0` for empty cells. Each row should be on a new line, with numbers separated by spaces.
   Example:
   ```sh
     5 3 0 0 7 0 0 0 0
     6 0 0 1 9 5 0 0 0
     0 9 8 0 0 0 0 6 0
     8 0 0 0 6 0 0 0 3
     4 0 0 8 0 3 0 0 1
     7 0 0 0 2 0 0 0 6
     0 6 0 0 0 0 2 8 0
     0 0 0 4 1 9 0 0 5
     0 0 0 0 8 0 0 7 9
   ```
3. Run the script:
   ```sh
   python solver.py
   ```
4. Input the filename: When prompted, enter the name of your input file (e.g., `sudoku_input.txt`).




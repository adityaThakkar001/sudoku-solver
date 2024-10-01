import os
import heapq

def read_matrix_from_input(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

def check_matrix(matrix):
    if len(matrix) != 9:
        return False
    for i in range(len(matrix)):
        if len(matrix[i]) != 9:
            return False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 9 or matrix[i][j] < 0:
                return False
    return True

def format_output(matrix):
    return '\n'.join(' '.join(map(str, row)) for row in matrix)

def is_valid(matrix, row, col, num):
    for x in range(9):
        if matrix[row][x] == num or matrix[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if matrix[i + start_row][j + start_col] == num:
                return False
    return True

def find_empty(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return (i, j)
    return None

def heuristic(matrix):
    return sum(row.count(0) for row in matrix)

def astar(matrix):
    open_set = []
    heapq.heappush(open_set, (heuristic(matrix), matrix))
    closed_set = set()

    while open_set:
        _, current_matrix = heapq.heappop(open_set)

        if tuple(map(tuple, current_matrix)) in closed_set:
            continue
        closed_set.add(tuple(map(tuple, current_matrix)))

        if heuristic(current_matrix) == 0:
            return current_matrix  

        empty_cell = find_empty(current_matrix)
        if empty_cell:
            row, col = empty_cell
            for num in range(1, 10):
                if is_valid(current_matrix, row, col, num):
                    new_matrix = [r[:] for r in current_matrix]
                    new_matrix[row][col] = num
                    heapq.heappush(open_set, (heuristic(new_matrix) + (9 - sum(row.count(0) for row in new_matrix)), new_matrix))

    return None

input_filename = input("Enter file name : ")
matrix = read_matrix_from_input(input_filename)

if check_matrix(matrix):
    output_matrix = astar(matrix)
    if output_matrix is not None:
        output = format_output(output_matrix)
    else:
        output = "No solution found."
else:
    output = "Enter Valid Sudoku!"

output_filename = os.path.splitext(input_filename)[0] + '_output.txt'

with open(output_filename, 'w') as output_file:
    output_file.write(output)

print(f"Output written to {output_filename}")

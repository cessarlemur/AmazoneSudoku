import random
import time
import math
import sys
import copy

 

def objective_score(board):
    #TODO: Implement the objective function to calculate the score of the board
    size = 9
    block_size = 3
    conflicts = 0
    
    # Check rows and columns for conflicts
    for i in range(size):
        for j in board[i]:
            if j == 0:
                conflicts += 1
    
    for i in range(size):
        row_numbers = []
        col_numbers = []
        for j in range(size):
            if board[i][j] != 0:
                if board[i][j] in row_numbers:
                    conflicts += 1
                else:
                    row_numbers.append(board[i][j])
            if board[j][i] != 0:
                if board[j][i] in col_numbers:
                    conflicts += 1
                else:
                    col_numbers.append(board[j][i])

    # Check 3x3 blocks for conflicts
    for i in range(0, size, block_size):
        for j in range(0, size, block_size):
            block_numbers = []
            for k in range(block_size):
                for l in range(block_size):
                    num = board[i+k][j+l]
                    if num != 0:
                        if num in block_numbers:
                            conflicts += 1
                        else:
                            block_numbers.append(num)

    return conflicts

 

 

def simulated_annealing_solver(initial_board):

    """Simulated annealing Sudoku solver."""

    current_solution = [row[:] for row in initial_board]
    best_solution = current_solution
    
    current_score = objective_score(current_solution)
    best_score = current_score

    temperature = 0.5
    cooling_rate = 0.99999  #TODO: Adjust this parameter to control the cooling rate
    imposed = []
    count = 0
    while 400000 > count:
        count += 1
        if (count % 1000 == 0):
            print("______________________________")
            print_board(current_solution)
            print("______________________________")

        try:  

            # TODO: Generate a neighbor (Don't forget to skip non-zeros tiles in the initial board ! It will be verified on Inginious.)
            # Choisissez une case aléatoire non fixée et modifiez sa valeur
            neighbor = copy.deepcopy(current_solution)
            while True:
                i = random.randint(0, 8)
                j = random.randint(0, 8)
                if initial_board[i][j] == 0:  # Vérifie que la case peut être modifiée
                    old_value = current_solution[i][j]
                    new_value = random.randint(1, 9)
                    while new_value == old_value:
                        new_value = random.randint(1, 9)
                    neighbor[i][j] = new_value
                    break
           

            # Evaluate the neighbor
            neighbor_score = objective_score(neighbor)

            # Calculate acceptance probability
            delta = float(current_score - neighbor_score)

            if current_score == 0:

                return current_solution, current_score

            # Accept the neighbor with a probability based on the acceptance probability
            if neighbor_score < current_score or (neighbor_score > 0 and math.exp((delta/temperature)) > random.random()):

                current_solution = neighbor
                current_score = neighbor_score

                if (current_score < best_score):
                    best_solution = current_solution
                    best_score = current_score

            # Cool down the temperature
            temperature *= cooling_rate
        except:

            print("Break asked")
            break
        
    return best_solution, best_score

 
def print_board(board):

    """Print the Sudoku board."""

    for row in board:
        print("".join(map(str, row)))

 

def read_sudoku_from_file(file_path):
    """Read Sudoku puzzle from a text file."""
    
    with open(file_path, 'r') as file:
        sudoku = [[int(num) for num in line.strip()] for line in file]

    return sudoku
 

if __name__ == "__main__":

    # Reading Sudoku from file
    initial_board = read_sudoku_from_file(sys.argv[1])

    # Solving Sudoku using simulated annealing
    start_timer = time.perf_counter()

    solved_board, current_score = simulated_annealing_solver(initial_board)

    end_timer = time.perf_counter()

    print_board(solved_board)
    print("\nValue(C):", current_score)

    # print("\nTime taken:", end_timer - start_timer, "seconds")
from IPython.display import clear_output
import time

#CONSTANTS

#cell coordinates will be stored as pairs of integers
#since a standard sudoku board comprises rows, columns and 3x3 "boxes",
#the two dictionaries below bind each cell coordinate pair to the 3x3 box it belongs to and vice versa  
BOX = {
    0:((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)), 
    1:((0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)), 
    2:((0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)),
    3:((3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)),
    4:((3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)),
    5:((3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)),
    6:((6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)),
    7:((6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)),
    8:((6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)) 
}

BOX_MAP = {
    (0,0):0,(0,1):0,(0,2):0,(1,0):0,(1,1):0,(1,2):0,(2,0):0,(2,1):0,(2,2):0, 
    (0,3):1,(0,4):1,(0,5):1,(1,3):1,(1,4):1,(1,5):1,(2,3):1,(2,4):1,(2,5):1, 
    (0,6):2,(0,7):2,(0,8):2,(1,6):2,(1,7):2,(1,8):2,(2,6):2,(2,7):2,(2,8):2,
    (3,0):3,(3,1):3,(3,2):3,(4,0):3,(4,1):3,(4,2):3,(5,0):3,(5,1):3,(5,2):3,
    (3,3):4,(3,4):4,(3,5):4,(4,3):4,(4,4):4,(4,5):4,(5,3):4,(5,4):4,(5,5):4,
    (3,6):5,(3,7):5,(3,8):5,(4,6):5,(4,7):5,(4,8):5,(5,6):5,(5,7):5,(5,8):5,
    (6,0):6,(6,1):6,(6,2):6,(7,0):6,(7,1):6,(7,2):6,(8,0):6,(8,1):6,(8,2):6,
    (6,3):7,(6,4):7,(6,5):7,(7,3):7,(7,4):7,(7,5):7,(8,3):7,(8,4):7,(8,5):7,
    (6,6):8,(6,7):8,(6,8):8,(7,6):8,(7,7):8,(7,8):8,(8,6):8,(8,7):8,(8,8):8 
}

#similarly, since rows will be labeled with letters for clarity,
#the two dictionaries below bind row numbers to letters and vice versa 
ROW_MAP = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i'}
ROW_REV_MAP = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8}

#EASY starting board to be loaded and viewed on startup
STARTING_BOARD = (
    (5,3,0,0,7,0,0,0,0),
    (6,0,0,1,9,5,0,0,0),
    (0,9,8,0,0,0,0,6,0),
    (8,0,0,0,6,0,0,0,3),
    (4,0,0,8,0,3,0,0,1),
    (7,0,0,0,2,0,0,0,6),
    (0,6,0,0,0,0,2,8,0),
    (0,0,0,4,1,9,0,0,5),
    (0,0,0,0,8,0,0,7,9)
)

#HARD
# STARTING_BOARD = (
#     (9,0,1,0,0,5,4,8,0),
#     (0,0,0,2,0,0,0,7,0),
#     (0,8,0,0,0,0,0,0,0),
#     (4,0,6,0,0,9,1,0,0),
#     (3,0,0,0,0,0,0,0,0),
#     (0,0,0,0,5,0,0,0,9),
#     (6,0,8,0,7,0,0,4,0),
#     (0,5,0,0,0,0,8,0,0),
#     (0,3,0,0,0,6,0,0,0)
# )


# def clear_board():
#     '''
#     Clears the board, making it effectively EMPTY (zero = empty cell)
#     '''
#     global board
#     board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]


def restart_board(STARTING_BOARD):
    '''
    Returns the initial state of the current puzzle (clearing all the player's modifications when assigned to board)
    '''
    return [list(row) for row in STARTING_BOARD]

def zeros_to_spaces(num):
    '''
    Empty cells contain the value of 0. When printing the board, zeros are changed to ' '
    '''
    if num == 0:
        return ' '
    else:
        return str(num)

def printer(board):
    '''
    Function to print a simple text-based depiction of the given board state.
    As requested in the original exercise, digits entered by the player (modifiable) are marked with '*' 
    '''
    clear_output()
    print('     (1) (2) (3) (4) (5) (6) (7) (8) (9)')
    print('    -------------------------------------')
    for i in range(9):
        for j in range(9):
            if j == 0:
                print(f'({ROW_MAP[i]}) | ', end="")
            elif j in [3,6]:
                print('‖ ', end="")
            else:
                print('| ', end="")
            print(zeros_to_spaces(board[i][j]),  end="")
            if board[i][j] == STARTING_BOARD[i][j]:
                print(' ',end="")
            else:
                print('*',end="")
        print('|')
        if i in [2,5]:
            print('    =====================================')
        else:
            print('    -------------------------------------')


def check_if_legal_loc(row,col,STARTING_BOARD):
    '''
    Function checks whether a move is legal, that is:
    if the row and col values are within the legal range (board size)
    AND if the chosen location is modifiable, i.e. was not originally filled in the puzzle's initial state (in the STARTING_BOARD)
    '''
    if row < 0 or row > 8:
        print('Row out of range')
        return False
    if col < 0 or col > 8:
        print('Column out of range')
        return False

    if STARTING_BOARD[row][col] == 0:
        return True
    else:
        print(f'Cell contained {STARTING_BOARD[row][col]} from the beginning; cannot be modified.')
        return False


def add_digit(board):
    '''
    Prompts user for input (row, column, digit to place), verifies it, returns the new board state with the digit added
    '''
    row = None
    col = None
    digit = None

    #while loop to get and verify the input, will repeat until valid input is provided:
    while row == None or col == None or digit == None:
        row_input = input('Input row (a-i) :' ).lower().strip()
        if row_input not in ROW_REV_MAP:
            print('Expected: a, b, c, d, e, f, g, h or i')
            continue
        else:
            row = ROW_REV_MAP[row_input]

        col_input = input('Input column (1-9): ')
        if not col_input.isdigit():
            print('Expected: natural numbers <1,9>')
            continue
        else:
            col = int(col_input)-1
        
        if not check_if_legal_loc(row,col,STARTING_BOARD): #if the location is "illegal", the while loop will start over again
            digit = None
        else:
            digit_input = input(f'Provide digit to be placed in the {ROW_MAP[row]}{col+1} cell (note: 0 = erase): ')
            if digit_input.isdigit():
                if int(digit_input) >= 0 and int(digit_input) <= 9:
                    digit = int(digit_input)
                else:
                    print('Out of range!')
            else:
                print('Provide a digit!')

    #Placement of the digit in the chosen cell
    if digit == 0:
        board[row][col] = 0
    else:
        board[row][col] = digit
    
    return board



def count_empty(board):
    '''
    Counts empty cells (zeros) in the board, going row by row
    If the returned count == 0, then the board is finished (filled)
    '''
    count = 0
    for i in board:
        count += i.count(0)
    return count


def verify(board):
    '''
    Verifies a (hopefully) solved board, checking validity in each row, each column, each 3x3 box
    Will also return False if there are any empty cells (zeros), since 0 is not in the desired set 
    '''
    result = True


    #check rows:
    for row in range(9):
        if set(board[row]) != {1,2,3,4,5,6,7,8,9}:
            print('Error in row', ROW_MAP[row])
            result = False

    #check columns:
    for col in range(9):
        if set([board[row][col] for row in range(9)]) != {1,2,3,4,5,6,7,8,9}:
            print('Error in column', col+1)
            result = False
    
    #check 3x3 boxes:
    for b in range(9):
        if set([board[row][col] for row, col in BOX[b]]) != {1,2,3,4,5,6,7,8,9}:
            print('Error in box', b+1)
            result = False

    return result 
    


def simple_solver(board):
    '''
    The most naive solver I could think of, solves sudoku like a child would do.
    Assumes there is a forced line of single-digits without splits, variants, advanced techniques etc.,
    iterating through board, looking for cells with only one possible candidate digit and filling them
    with the obvious candidate until no further improvement is possible.
    DOES NOT GUARANTEE A SOLUTION WILL BE FOUND, works only with the easiest puzzles.
    Returns the obtained board state (either fully or partially solved).
    '''
    start_time = time.time()
    improvement = True
    while improvement:
        improvement = False
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    row_candidates = {1,2,3,4,5,6,7,8,9} - set(board[row])
                    col_candidates = {1,2,3,4,5,6,7,8,9} - set([board[r][col] for r in range(9)])
                    b = BOX_MAP[(row, col)]
                    box_candidates = {1,2,3,4,5,6,7,8,9} - set([board[r][c] for r, c in BOX[b]])
                    cell_candidates = row_candidates & col_candidates & box_candidates
                    if len(cell_candidates) == 1:
                        improvement = True
                        digit, = cell_candidates   #set unpacking
                        board[row][col] = digit
    solving_time = time.time() - start_time
    if count_empty(board) == 0:
        print(f'Simple solver was good enough to solve the puzzle. Spent {solving_time} s')
    else:
        print(f'Simple solver could not fill in {count_empty(board)} cells. Spent {solving_time} s')
    return board
                    

def brute_solver():
    '''
    Unstoppable solver, coming soon
    '''
    pass



# The program loop

game_on = True

board = restart_board(STARTING_BOARD)

while game_on:
    print('\n')
    printer(board)
    print('enter = input another digit;\n X = check if solved correctly;\n C = restart puzzle; \n S = simple solver; \n Q = quit;')
    choice = input('Your choice: ')
    if choice.lower() == 'q':
        print('--------program ended---------')
        game_on = False
    elif choice.lower() == 'x':
        if verify(board):
            print('SOLUTION CORRECT!!! \n -----program ended------')
            game_on = False
        else:
            print('INCORRECT, TRY AGAIN.')
    
    elif choice.lower() == 'c':
        board = restart_board(STARTING_BOARD)

    elif choice.lower() == 's':
        board = simple_solver(board)
        game_on = True
    else:
        printer(board)
        board = add_digit(board)
        





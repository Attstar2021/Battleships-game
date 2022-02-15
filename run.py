import random
import time
"""
Declared global veriable for battleships game.
"""
BOARD = [[]]
board_size = 7
num_of_ships = 5
ship_placement = [[]]
fire_left = 10
ship_sunk = 0
game_over = False
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_board():
    """
    to create a board and to place ships of 
    different sizes on gird.
    """
    global board_size
    global BOARD
    global num_of_ships
    global ship_placement

    random.seed(time.time())
    rows, cols = (board_size, board_size)
    BOARD = []
    row = []
    for r in range(rows):
        row.append(".")
    for c in range(cols):
        BOARD.append(row)
    num_of_ships_placed = 0
    ship_placement = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(1, 3)
        if place_ship(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1


def validate_board(x1, x2, y1, y2):
    """
    To place ship inside the grid.
    """
    global ship_placement
    global BOARD

    all_valid = True
    for r in range(x1, x2):
        for c in range(y1, y2):
            if BOARD[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_placement.append([x1, x2, y1, y2])
        for r in range(x1, x2):
            for c in range(y1, y2):
                BOARD[r][c] = "O"
    return all_valid


def place_ship(row, col, direction, length):
    """
    To place a ship on board with helper.
    """
    global board_size

    x1, x2, y1, y2 = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        y1 = col - length + 1
    elif direction == "right":
        if col + length >= board_size:
            return False
        y2 = col + length
    elif direction == "up":
        if row - length < 0:
            return False
        x1 = row - length + 1
    elif direction == "down":
        if row + length >= board_size:
            return False
        x2 = row + length

    return validate_board(x1, x2, y1, y2)


def print_board():
    """
    Help to print the board with rows and columns.
    """
    global BOARD
    global alphabet
    debug_mode = True

    alphabet = alphabet[0: len(BOARD) + 1]

    for row in range(len(BOARD)):
        print(alphabet[row], end=") ")
        for col in range(len(BOARD[row])):
            if BOARD[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(BOARD[row][col], end=" ")
        print("")

    print(" ", end=" ")
    for i in range(len(BOARD[0])):
        print(str(i), end=" ")
    print(" ")


def fire_placement():
    """
    To get valid row and column to place a bullet shot.
    """
    global BOARD
    global alphabet

    is_valid_placement = False
    row = -1 
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-G) and column (0-6) such as A3:")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter again.. for example B2.")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter again.. for example A3.")
            continue
        row = alphabet.find(row)
        if not (-1 < row < board_size):
            print("Error: Please enter again for example B2.")
            continue
        col = int(col)
        if not (-1 < col < board_size):
            print("Error: Please enter again for example C4.")
            continue
        if BOARD[row][col] == "#" or BOARD[row][col] == "X":
            print("You have already shot a bullet here, please try somewhere else")
            continue
        if BOARD[row][col] == "." or BOARD[row][col] == "O":
            is_valid_placement = True

    return row, col


def shoot_a_fire():
    """
    Update score board.
    """
    global BOARD 
    global ship_sunk 
    global fire_left

    row, col = fire_placement()
    print("")
    print("---------------------------")
    if BOARD[row][col] == ".":
        print("You missed")
        BOARD[row][col] = "#"
    elif BOARD[row][col] == "O":
        print("BZ you hit a ship!", end=" ")
        BOARD[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("Hurrah! A ship was completely sunk")
            ship_sunk += 1
        else:
            print("A ship was shot")
    fire_left -= 1




def check_for_ship_sunk():
    """
    This help to find ship and to check if it is completely sunk.
    """
    global ship_placement 
    global BOARD
    for position in ship_placement:
        x1 = position[0]
        x2 = position[1]
        y1 = position[2]
        y2 = position[3]
        if x1 <= row <= x2 and y1 <= col <= y2:
            for r in range(x1, x2):
                for c in range(y1, y2):
                    if BOARD[r][c] != "X":
                        return False
    return True


def gameover():
    """
    If all ships sunk or runs out of fire then game over.
    """
    global num_of_ships
    global fire_left 
    global game_over

    if num_of_ships == ship_sunk:
       print("Congrats you win!")
       game_over = True
    elif fire_left <= 0:
        print("Oops! you ran out of bullets, try again next time")
        game_over = True


def main():
    """
    Main function helps to runs the game loop.
    """
    global game_over
    player_name = input("please enter your name:\n")
    print("Welcome to Battleships game!")
    print(f"{player_name} you have 10 bullets to take down ships, lets begin!")
    create_board()

    while game_over is False:
        print_board()
        print("Number of ships remaining: " + str(num_of_ships - ship_sunk))
        print("Number of bullets left: " + str(fire_left))
        shoot_a_fire()
        print("----------------------------")
        print("")
        gameover()


main()







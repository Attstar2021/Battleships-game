import time
import random

"""
Declared global variable for battleships game.
"""

BOARD = [[]]
SHIP_PLACEMENT = [[]]
BOARD_SIZE = 8
NUM_OF_SHIPS = 2
FIRE_LEFT = 10
SHIP_SUNK = 0
GAME_OVER = False
ALPHABET = "ABCDEFGH"


def create_board():
    """
    to create a board and to place ships of
    different sizes on gird.
    """
    global BOARD
    global SHIP_PLACEMENT

    random.seed(time.time())
    rows, cols = (BOARD_SIZE, BOARD_SIZE)
    BOARD = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        BOARD.append(row)
    total_ships = 0
    SHIP_PLACEMENT = []

    while total_ships != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(1, 3)
        if place_a_ship(random_row, random_col, direction, ship_size):
            total_ships += 1


def validate_board(x_1, x_2, y_1, y_2):
    """
    To place ship inside the grids.
    """
    all_valid = True
    for r in range(x_1, x_2):
        for c in range(y_1, y_2):
            if BOARD[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        SHIP_PLACEMENT.append([x_1, x_2, y_1, y_2])
        for r in range(x_1, x_2):
            for c in range(y_1, y_2):
                BOARD[r][c] = "O"
    return all_valid


def place_a_ship(row, col, direction, length):
    """
    Display and place ship in grid.
    """

    x_1, x_2, y_1, y_2 = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        y_1 = col - length + 1
    elif direction == "right":
        if col + length >= BOARD_SIZE:
            return False
        y_2 = col + length
    elif direction == "up":
        if row - length < 0:
            return False
        x_1 = row - length + 1
    elif direction == "down":
        if row + length >= BOARD_SIZE:
            return False
        x_2 = col + length

    return validate_board(x_1, x_2, y_1, y_2)


def fire_placement():
    """
    To get valid row and column to place a shot.
    """

    valid_placement = False
    row = -1
    col = -1
    while valid_placement is False:
        placement = input("Enter row (A-H) and column (0-7) such as A1: ")
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print("Error: Please enter again.. for example B2.")
            continue
        if len(placement) <= 1 or len(placement) == ALPHABET:
            print("Error: Enter row (A-H) and column (0-7) for example B2.")
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print("Error: Please enter again.. for example A3.")
            continue
        row = ALPHABET.find(row)
        if not (-1 < row < BOARD_SIZE):
            print("Error: Please enter again for example B2.")
            continue
        col = int(col)
        if not (-1 < col < BOARD_SIZE):
            print("Error: Please enter again for example C4.")
            continue
        if BOARD[row][col] == "#" or BOARD[row][col] == "X":
            print("You have already shot here, please try another place.")
            continue
        if BOARD[row][col] == "." or BOARD[row][col] == "O":
            valid_placement = True

    return row, col


def display_board():
    """
    Help to print the board with rows and columns.
    """
    global ALPHABET
    debug_mode = True

    ALPHABET = ALPHABET[0: len(BOARD) + 1]

    for row in range(len(BOARD)):
        print(ALPHABET[row], end=") ")
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


def shoot_a_fire():
    """
    Update score board.
    """
    global SHIP_SUNK
    global FIRE_LEFT
    row, col = fire_placement()
    print("")
    print("---------------------------")
    if BOARD[row][col] == ".":
        print("You missed")
        BOARD[row][col] = "#"
    elif BOARD[row][col] == "O":
        print("BZ you hit a ship!", end=" ")
        BOARD[row][col] = "X"
        if ship_sunk(row, col):
            print("Hurrah! That ship completely sunk")
            SHIP_SUNK += 1
        else:
            print("A ship was shot")
    FIRE_LEFT -= 1


def ship_sunk(row, col):
    """
    This help to find ship and to check if it is completely sunk.
    """

    for position in SHIP_PLACEMENT:
        x_1 = position[0]
        x_2 = position[1]
        y_1 = position[2]
        y_2 = position[3]
        if x_1 <= row <= x_2 and y_1 <= col <= y_2:
            for r in range(x_1, x_2):
                for c in range(y_1, y_2):
                    if BOARD[r][c] != "X":
                        return False
    return True


def game_over():
    """
    If all ships sunk or runs out of fire then game over.
    """
    global GAME_OVER

    if NUM_OF_SHIPS == SHIP_SUNK:
        print("Congrats you win!")
        GAME_OVER = True
    elif FIRE_LEFT <= 0:
        print("Oops! you ran out of bullets, try again next time")
        GAME_OVER = True


def main():
    """
    Main function helps to runs the game loop.
    """

    player_name = input("please enter your name:\n")
    print("*** Welcome to Battleships Game ***")
    print(f"{player_name.capitalize()} you have 10 fire to take down 2 ships.")
    print("Let's start our game!")

    create_board()

    while GAME_OVER is False:
        display_board()
        print("Number of ships remaining: " + str(NUM_OF_SHIPS - SHIP_SUNK))
        print("Number of bullets left: " + str(FIRE_LEFT))
        shoot_a_fire()
        print("----------------------------")
        print("")
        game_over()


main()

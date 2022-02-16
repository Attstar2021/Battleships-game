import random
from random import randint
import time
"""
Declared global variable for battleships game.
"""
board = [[]]
BOARD_SIZE = 5
NUM_OF_SHIPS = 1
ship_placement = [[]]
FIRE_LEFT = 1
ship_sunk = 0
game_over = False
alphabet = "ABCDE"


def create_board():
    """
    to create a board and to place ships of
    different sizes on gird.
    """
    global board
    global ship_placement

    random.seed(time.time())
    rows, cols = (BOARD_SIZE, BOARD_SIZE)
    board = []
    row = []
    for r in range(rows):
        row.append(".")
    for c in range(cols):
        board.append(row)
    num_of_ships_placed = 0
    ship_placement = []

    while num_of_ships_placed != NUM_OF_SHIPS:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(1, 3)

        if place_ship(random_row):
            num_of_ships_placed += 1


def validate_board(x1, x2, y1, y2):
    """
    To place ship inside the grid.
    """
    global ship_placement
    all_valid = True
    for r in range(x1, x2):
        for c in range(y1, y2):
            if board[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_placement.append([x1, x2, y1, y2])
        for r in range(x1, x2):
            for c in range(y1, y2):
                board[r][c] = "O"
    return all_valid

    return validate_board(x1, x2, y1, y2)


def place_ship(row):
    return randint(0, row - 1)


def print_board():
    """
    Help to print the board with rows and columns.
    """
    global alphabet
    debug_mode = True

    alphabet = alphabet[0: len(board) + 1]

    for row in range(len(board)):
        print(alphabet[row], end=") ")
        for col in range(len(board[row])):
            if board[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(board[row][col], end=" ")
        print("")

    print(" ", end=" ")
    for i in range(len(board[0])):
        print(str(i), end=" ")
    print(" ")


def fire_placement():
    """
    To get valid row and column to place a bullet shot.
    """
    global alphabet

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input("Enter row (A-E) and column (0-4) such as A3:")
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
        if not (-1 < row < BOARD_SIZE):
            print("Error: Please enter again for example B2.")
            continue
        col = int(col)
        if not (-1 < col < BOARD_SIZE):
            print("Error: Please enter again for example C4.")
            continue
        if board[row][col] == "#" or board[row][col] == "X":
            print("You have already shot a bullet here!")
            continue
        if board[row][col] == "." or board[row][col] == "O":
            is_valid_placement = True

    return row, col


def shoot_a_fire():
    """
    Update score board.
    """
    global ship_sunk
    global FIRE_LEFT
    row, col = fire_placement()
    print("")
    print("---------------------------")
    if board[row][col] == ".":
        print("You missed")
        board[row][col] = "#"
    elif board[row][col] == "O":
        print("BZ you hit a ship!", end=" ")
        board[row][col] = "X"
        if check_for_ship_sunk(row, col):
            print("Hurrah! A ship was completely sunk")
            ship_sunk += 1
        else:
            print("A ship was shot")
    FIRE_LEFT -= 1


def check_for_ship_sunk(row, col):
    """
    This help to find ship and to check if it is completely sunk.
    """
    global ship_placement
    for position in ship_placement:
        x1 = position[0]
        x2 = position[1]
        y1 = position[2]
        y2 = position[3]
        if x1 <= row <= x2 and y1 <= col <= y2:
            for r in range(x1, x2):
                for c in range(y1, y2):
                    if board[r][c] != "X":
                        return False
    return True


def gameover():
    """
    If all ships sunk or runs out of fire then game over.
    """
    global FIRE_LEFT
    global game_over

    if NUM_OF_SHIPS == ship_sunk:
        print("Congrats you win!")
        game_over = True
    elif FIRE_LEFT <= 0:
        print("Oops! you ran out of bullets, try again next time")
        game_over = True


def main():
    """
    Main function helps to runs the game loop.
    """
    player_name = input("please enter your name:\n")
    print("Welcome to Battleships game!")
    print(f"{player_name} you have 1 bullet to take down ships, lets begin!")
    create_board()

    if game_over is False:
        print_board()
        print("Number of ships remaining: " + str(NUM_OF_SHIPS - ship_sunk))
        print("Number of bullets left: " + str(FIRE_LEFT))
        shoot_a_fire()
        print("----------------------------")
        print("")
        gameover()


main()

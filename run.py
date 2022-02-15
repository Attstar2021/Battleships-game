import randon
import time
"""
Declared global veriable for battleships game.
"""
board =[[]]
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
    global board
    global num_of_ships
    global ship_placement

    random.seed(time.time())
    rows, cols = (board_size, board_size)
    board = []
    row = []
    for r in range(rows):
        row.append(".")
    for c in range(cols):
        board.append(row)
    num_of_ships_placed = 0
    ship_placement = []

    while num_of_ships_placed != num_of_ships
        random_row = random.randint(0,rows - 1)
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
    global board

    all_valid = True
    for r in range(x1, x2):
        for c in range(y1, y2):
            if board[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_placement.append([x1, x2, y1, y2])
        for r in range(x1, x2):
            for c in range(y1,y2):
                board[r][c] = "O"
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
        if col = length >= board_size:
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


def fire_placement():

def shoot_a_fire():
def check_for_ship_sunk():



def gameover():


def main():
    """
    Main function helps to runs the game loop.
    """
    create_board()







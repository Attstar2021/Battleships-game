import randon
import time
"""
Declared global veriable for battleships game.
"""
board =[[]]
board_size = 10
num_of_ships = 5
ship_placement = [[]]
fire_left = 10
ship_sunk = 0
game_over = False
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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

def place_ship():


def create_board():


def print_board():


def fire_placement():


def check_for_ship_sunk():


def shoot_a_fire():


def gameover():


def main():







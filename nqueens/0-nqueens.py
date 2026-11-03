#!/usr/bin/python3

# class Queen:
#     def __init__(self)

def create_board(n: int):
    # check if int
    # check greater than 4

    board = []
    x = 0
    for square in range(n):
        row = []
        for y in range(n):
            row.append([x, y])
            y += 1
        board.append(row)
        x += 1
    return board

def can_attack(position, defender) -> bool:
    if position == None:
        return True
    # horiztonal
    if position[0] == defender[0]:
        return True
    # vertical
    if position[1] == defender[1]:
        return True
    # diagonal down right
    if position[0] - defender[0] == position[1] - defender[1]:
        return True
    # diagonal up right
    if position[0] - defender[0] == defender[1] - position[1]:
        return True
    # diagonal down left
    if defender[0] - position[0] == position[1] - defender[1]:
        return True
    # diagonal up left
    if position[0] - defender[0] == position[1] - defender[1]:
        return True

def find_next_queen(queens, board, square):
    if not queens:
        return square
    for row in board:
        for square1 in row:
            for queen in queens:
                if can_attack(queen, square1):
                    break
                if queens.index(queen) == len(queens) - 1:
                    return square1
    return None
def solve_square(queens, square, board, n):
    for row in board:
        for square in row:
            next_queen = find_next_queen(queens, board, square)
            if next_queen != None:
                queens.append(next_queen)
            if len(queens) == n:
                return queens
    return None



def check_row(queens, row, board, n):
    for square in row:
        queens = solve_square(queens, square, board, n)
        if queens != None:
            return queens
    return None

n = 4
board = create_board(n)
for row in board:
    print(row)


solutions = []
queens = []


for row in board:
    queens = check_row(queens, row, board, n)
    if queens != None:
        solutions.append(queens)


for solution in solutions:
    print(solution)


# for square in board[0]:
#     queens = []
#     print(f"appending {square} to {queens}")
#     queens.append(square)

#     for square1 in board[1]:
#         potential = solve_square(queens, square1, board, n)
#         if potential is not None:
#             solutions.append(potential)
#             break

# NEED TO RECURSIVELY CALL ABOVE
# IF IT THE SOLUTION IS NOT THE NEXT QUEEN CHECK THE NEXT SQUARE IN ROW
# SOMETHING LIKE 



        
# def r_solve_square(queens, square, board, n):
#     if square == [n - 1, n - 1]:
#         return None
#     if len(queens) == n:
#         return queens
#     if not queens:
#         return square
#     next_queen = find_next_queen(queens, board, square)
#     if not next_queen:
#         return None
#     while queens != None or len(queens) == n:
#         queens = r_solve_square(queens, square, board, n)
#         if not queens:
#             return None
#     return queens
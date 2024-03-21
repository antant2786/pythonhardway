def generate_plinko_board(num_slots, num_rows, x_location):
    # Create an empty grid
    grid = [[' ' for _ in range(num_slots * 2 + 1)] for _ in range(num_rows)]

    # Place pegs on the grid with shifting
    for row in range(num_rows):
        shift = row % 2  # Shift pegs for alternate rows
        for col in range(num_slots * 2 + 1):
            if col % 2 == shift:
                if (row, col) == x_location:
                    grid[row][col] = 'O'
                else:
                    grid[row][col] = ' '
            else:
                grid[row][col] = '.'

    return grid





def print_plinko_board(board):
    for row in board:
        print(''.join(row))





if __name__ == "__main__":
    num_slots = 20  # Number of slots
    num_rows = 10  # Number of rows
    x_location = (4, 6)

    plinko_board = generate_plinko_board(num_slots, num_rows, x_location)
    print_plinko_board(plinko_board)

import utils

boards = []
sequence = []


def day4(lines):
    sequence = utils.str_to_int_arr(lines[0], ',')
    print(sequence)

    board = []
    for line in lines[2:]:
        if line == '':
            if len(board) > 0:
                boards.append(board)
            board = []
        else:
            board.append(utils.str_to_int_arr(line))
    boards.append(board)

    for i in range(len(sequence)):
        is_bingo = check_boards(sequence[:i])
        if is_bingo != False:
            calc_score(sequence[:i], board)
            break

    for i in range(len(sequence)):
        bingo_board = check_boards(sequence[:i])
        while bingo_board:
            boards.remove(bingo_board)

            if len(boards) == 0:
                calc_score(sequence[:i], bingo_board)
                return
            bingo_board = check_boards(sequence[:i])


def check_boards(draw):
    for board in boards:
        if check_board(draw, board):
            return board
    return False


def check_board(draw, board):
    if check_columns(draw, board) or check_rows(draw, board):
        return True


def check_columns(draw, board):
    for i in range(5):
        col = []
        for j in range(5):
            col.append(board[j][i])
        if check_arr(draw, col):
            return True


def check_rows(draw, board):
    for i in range(5):
        if check_arr(draw, board[i]):
            return True


def check_arr(draw, row):
    count = 0
    for r in row:
        if r in draw:
            count += 1
    return count == 5


def calc_score(draw, board):
    numbers = []
    for i in range(5):
        for j in range(5):
            number = board[i][j]
            if not number in draw:
                numbers.append(number)

    print('BINGO!')
    print('sum:', sum(numbers), 'last draw:', draw[-1])
    print(sum(numbers) * draw[-1])

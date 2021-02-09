def unique_rows(board):
    for row in board:
        for char in row:
            if char not in ('*', ' '):
                if row.count(char) > 1:
                    return False
    return True


def unique_columns(board):
    columns = ['' for _ in board]
    for row in board:
        for i in range(len(row)):
            columns[i] += row[i]
    return unique_rows(columns)


def color_group(board):
    colors = []
    for row in range(4, len(board)):
        clr = ''
        dif = row - 4
        start = 4 - dif
        for ch in range(start, start+5):
            clr += board[row][ch]
        colors.append(clr)
    for ch in range(4, -1, -1):
        clr = ''
        start = 4 - ch
        for row in range(start, start+4):
            clr += board[row][ch]
        colors[start] += clr
    return colors


def unique_colors(board):
    return unique_rows(color_group(board))


def validate_board(board):
    return unique_rows(board) and unique_colors(board) \
           and unique_columns(board)
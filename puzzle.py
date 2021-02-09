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
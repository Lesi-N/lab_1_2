'''
Checks if game board is appropriate for gameplay
Github repository: https://github.com/Lesi-N/lab_1_2.git
'''

def unique_rows(board):
    '''
    Checks uniqueness of numbers in rows
    >>> unique_rows(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    True
    '''
    for row in board:
        for char in row:
            if char not in ('*', ' '):
                if row.count(char) > 1:
                    return False
    return True


def unique_columns(board):
    '''
    Checks uniqueness of numbers in columns
    >>> unique_columns(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    False
    '''
    columns = ['' for _ in board]
    for row in board:
        for i in range(len(row)):
            columns[i] += row[i]
    return unique_rows(columns)


def color_group(board):
    '''
    Groups numbers of different colors
    >>> color_group(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    [' 9 5   31', ' 83  1   ', '  1   4  ', ' 8  2  6 ', '  2    3 ']
    '''
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
    '''
    Checks uniqueness of numbers in color groups
    >>> unique_colors(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    True
    '''
    return unique_rows(color_group(board))


def validate_board(board):
    '''
    Checks if starting board is compliant with the rules
    >>> validate_board(["**** ****",\
    "***1 ****",\
    "**  3****",\
    "* 4 1****",\
    "     9 5 ",\
    " 6  83  *",\
    "3   1  **",\
    "  8  2***",\
    "  2  ****"])
    False
    '''
    return unique_rows(board) and unique_colors(board) \
           and unique_columns(board)

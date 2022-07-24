
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


sol = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
       ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
       ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
       ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
       ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
       ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
       ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
       ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
       ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]


def row(row_position):
    numbers = []
    for element in row_position:
        if element != ".":
            numbers.append(element)
    return numbers


def column(colum_position):
    numbers = []
    for element in colum_position:
        if element != ".":
            numbers.append(element)
    return numbers

def find_not_found_row(line):
    result = []
    for i in range(1, 10):
        if str(i) in line:
            pass
        else:
            result.append(str(i))
    return result

def find_not_found_col(posit):
    vertical = share_col(posit)
    result = []
    for i in range(1, 10):
        if str(i) in vertical:
            pass
        else:
            result.append(str(i))
    return result

def share_col(position_col):
    col = []
    # border[i][position_col]
    for ele in range(0, 10):
        col.append(board[ele][position_col])
    return col
for j in range(0, 10):
    pass
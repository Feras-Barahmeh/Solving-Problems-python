# # Input: s = "PAYPALISHIRING", numRows = 3

# # Output: "PAHNAPLSIIGYIR"

text = "PAYPALISHIRING"

key = 4

# n = ''

# # [A, Y, P, A, L, S, H, I, R, I, G]

# # [Y, P, A, H, R, I]

# # [P, I]


# # P     I    N

# # A   L S  I G

# # Y A   H R
# # P     I


value = [""] * key

num_row = 0

direc = 1

for i in range(len(text)):

    value[num_row] = value[num_row] + text[i]

    if num_row != key - 1 and direc == 1:

        num_row += 1

    else:

        if num_row > 0 and direc == -1:

            num_row -= 1

        else:

            direc *= -1

            num_row += direc


print(value)

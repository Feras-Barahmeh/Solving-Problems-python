length = int(input())
vector = str(input())
vector = list(vector.split(" "))

def cout(arr):
    for element in arr:
        if element != arr[-1]:
            print(element, end=" ")
        else:
            print(element, end="")
# Main
for i in range(len(vector) -1):
    for j in range(len(vector)- i -1):
        if j + 1 != len(vector):  # For pass out range error
            if vector[j] > vector[j + 1]:
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

cout(vector)
# 79
# 63 -8 -93 -90 -97 41 31 95 2 68 0 27 36 98 16 -9 28 72 -72 -12 -86 -1 -10 44 89 -61 -34 37 65 -77 79 76 -22 -28 2 -79 14 -82 8 -35 -65 60 -91 22 54 74 -77 47 -74 67 76 -57 -69 83 -36 -45 -24 -62 81 -45 23 69 94 37 -79 -2 -76 62 25 97 53 48 -31 -24 -37 -17 -79 -22 -4
# 64 34 25 12 22 11 90
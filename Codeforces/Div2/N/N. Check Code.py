left, right = [int(x) for x in input().split()]
equation = input()
x = equation.split("-")
if len(x[0]) == left and len(x[1]) == right:
    print("Yes")
else:
    print("No")
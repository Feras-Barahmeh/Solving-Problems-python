test_cases = int(input())
for i in range(test_cases):
    case = int(input())
    if case % 2 != 0:
        print(case//2)
    else:
        print(int(case/2) - 1)


# https://codeforces.com/contest/1642/problem/A


for _ in range(int(input())):
    x1, y1 = tuple(map(int, input().split()))
    x2, y2 = tuple(map(int, input().split()))
    x3, y3 = tuple(map(int, input().split()))

    max_y = max(y1, y2, y3)
    if max_y == y1 and max_y == y2:
        print(abs(x1 - x2))
    elif max_y == y1 and max_y == y3:
        print(abs(x1 - x3))
    elif max_y == y2 and max_y == y3:
        print(abs(x2 - x3))
    else:
        print(0)


# def slope(x1, y1, x2, y2):
#     return float(y2-y1)/float(x2-x1)
#
# n = int(input()); count = 0
#
# for i in range(n):
#     t = tuple(input().split())
#     t2 = tuple(input().split())
#     t3 = tuple(input().split())
#     if int(t2[0]) - int(t[0]) == 0 or int(t2[0]) - int(t3[0]) == 0 or int(t[0]) - int(t3[0]) == 0:
#         print(max(t[1], t2[1], t3[1]))
#         continue
#
#     slop1 = slope(int(t[0]), int(t[1]), int(t2[0]), int(t2[1]))
#     slop2 = slope(t2[0], t2[1], int(t3[0]), int(t3[1]))
#     slop3 = slope(t[0], t[1], int(t3[0]), int(t3[1]))
#     for j in range(3):
#         if slop2 == 2 or slop3 == 2 or slop1 == 2:
#             count += 1
#         if count >= 2:
#             print(0)
#         else:
#             print(max(t[1], t2[1], t3[1]))
#


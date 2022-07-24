# https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())
for i in range(n):
        if i % 2==0:
            print("#"*m)
        elif i % 4==1:
            print("." * (m-1) + "#")
        else:
            print("#" + "." * (m-1))


# n, m = map(int, input().split())
# temp = 1; side = 'r'
# line = ''
# for i in range(n):
#     for char in range(1, m+1):
#
#         if temp % 2 != 0:
#             line += "#"
#             if side == 'l':
#                 side = 'r'
#             else:
#                 side = 'l'
#         else:
#             if side == 'r' and char == 1:
#                 line += "#"
#             elif side == 'l' and char == m:
#                 line += '#'
#             else:
#                 line += "."
#
#     print(line)
#     line = ''
#     temp += 1

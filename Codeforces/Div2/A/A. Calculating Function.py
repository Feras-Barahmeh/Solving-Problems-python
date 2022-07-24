# https://codeforces.com/problemset/problem/486/A
# n = int(input())
def f(n):
    if n % 2 == 0:
        print(int(n / 2))
    else:
        print(-1 * n // 2)
# re = 0
# for i in range(0, n+1):
#     if i % 2== 0:
#         re += i
#     else:
#         re += -i
# print(re)
f(int(input()))
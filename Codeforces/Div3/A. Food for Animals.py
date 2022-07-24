# https://codeforces.com/contest/1675/problem/0

t = int(input())
for i in range(t):
    a, b, c, x, y = map(int, input().split())
    n = abs(x - a)
    nn = abs(y - b)

    if n + nn <= c:
        print("YES")
    else:
        print("NO")
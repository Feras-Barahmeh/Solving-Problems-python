# https://codeforces.com/problemset/problem/405/A
n = int(input())
col = [int(x) for x in input().split()]
col = sorted(col)
print(*col)
# https://codeforces.com/problemset/problem/1328/A
for _ in range(int(input())):
    a, b=map(int, input().split())
    print((b - a % b) % b)
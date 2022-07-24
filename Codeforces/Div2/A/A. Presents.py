# https://codeforces.com/problemset/problem/136/A

n = int(input())
pi = [str(x) for x in input().split()]
for i in range(1, n + 1):
    print(pi.index(str(i))+1, end=" ")
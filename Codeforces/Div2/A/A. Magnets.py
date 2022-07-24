# https://codeforces.com/problemset/problem/344/A
n = int(input())
counter = 0
g = ' '

for i in range(n):
    state = input()
    if state[1] != g[len(g)- 1]:
        counter += 1
    g += state

print(counter)
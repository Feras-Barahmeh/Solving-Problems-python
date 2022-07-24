# https://codeforces.com/problemset/problem/750/A

n, k = map(int, input().split())
z = 0
for i in range(1, n+1): z += 5*i
if (k + z) / 60 <= 4 :
    print(n)
else:
    cont = n
    while cont:
        z -= 5*cont
        n -= 1
        if (k + z) / 60 <= 4:
            print(n)
            break
        cont -= 1
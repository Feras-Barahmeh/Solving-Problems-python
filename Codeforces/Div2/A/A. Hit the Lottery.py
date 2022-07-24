# https://codeforces.com/problemset/problem/996/A
n = int(input())
count = 0
while n != 0:
    if n >= 100:
        count += int(n//100)
        n -= (int(n //100) *100)
    elif n >= 20:
        count += int(n // 20)
        n -= (int(n//20) * 20)
    elif n >= 10:
        count += int(n // 10)
        n -= int(n // 10) * 10
    elif n >=5:
        count += int(n // 5)
        n -= int(n // 5) * 5
    elif n >= 1:
        count += int(n//1)
        n -= int(n // 1) * 1
print(count)
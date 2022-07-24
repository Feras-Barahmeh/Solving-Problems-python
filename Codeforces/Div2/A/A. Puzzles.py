# https://codeforces.com/problemset/problem/337/A
n, m = map(int, input().split())
fi = [int(x) for x in input().split()]

fi = sorted(fi)
left = right = 0
temp = fi[n-1] - fi[0]
for i in range(len(fi)+n):
    if i == m - n + 1:
        break
    left = fi[i]
    right = fi[(i+n-1) % m]

    if temp > (right - left):
        temp = right - left
print(abs(temp))
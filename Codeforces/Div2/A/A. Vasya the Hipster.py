# https://codeforces.com/problemset/problem/581/A
a, b = map(int, input().split())
print(min(a, b), end=" ")
# print(int(abs(a-b)/2) if abs(a-b) // 2 >= 1 else  print(0))
if abs(a-b) // 2 >= 1:
    print(int(abs(a-b)/2), end="")
else:
    print(0, end="")

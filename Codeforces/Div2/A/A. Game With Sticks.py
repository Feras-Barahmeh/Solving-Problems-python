# https://codeforces.com/problemset/problem/451/A

row_stick, col_stick = map(int, input().split())

print("Malvika" if min(row_stick, col_stick) % 2 == 0 else "Akshat")
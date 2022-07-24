# https://codeforces.com/problemset/problem/339/B
n, m = map(int, input().split())
ai = [int(x) for x in input().split()]
count = 0
ptr = 1
# 3 2 3
# 1 → 2 → 3 →  4 → 1 → 2 → 3
for i in range(len(ai)):

    if i == 0:
        count += ai[i] - ptr
        ptr = ai[0]
    elif ptr == ai[i]:
        count += 0
    elif ai[i] < ptr:
        count += (n-ptr+ai[i]) % n
        ptr = ai[i]
    else:
        count += ai[i] - ptr
        ptr = ai[i]
print(count)

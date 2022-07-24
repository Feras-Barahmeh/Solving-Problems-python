# https://codeforces.com/problemset/problem/580/A
n = int(input())
ai = [int(x) for x in input().split()]
count = 0
result = []
for i in range(len(ai) + 1):
    if i + 1 < len(ai):
        if ai[i] <= ai[i + 1]:
            count += 1
        else:
            result.append(count)
            count = 0
    else:
        result.append(count)




print(max(result)+1)
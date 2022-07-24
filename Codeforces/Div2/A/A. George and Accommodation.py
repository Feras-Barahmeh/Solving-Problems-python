count = 0
for i in range(int(input())):
    pi, qi = map(int, input().split())
    if pi + 2 <= qi:
        count += 1
print(count)
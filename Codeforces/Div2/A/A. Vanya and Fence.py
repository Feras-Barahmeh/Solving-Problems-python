n, h = map(int, input().split())
ai = [int(x) for x in input().split()]
counter = 0
for i in ai:
    if i > h:
        counter += 2
    else:
        counter += 1
print(counter)
x = int(input())
center = int(0)
i = 1
while i <= x:
    center += 5
    if center >= x:
        print(i)
        break
    i += 1

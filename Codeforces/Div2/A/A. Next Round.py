num_contestant, grade_num = input().split()
degrees = [int(x) for x in input().split()]
counter = int(0)

for key, degree in enumerate(degrees):
    if degrees[key] >= degrees[int(grade_num) - 1] and degrees[key] > 0 and int(grade_num) > 0:
        counter += 1

print(counter)

iteration = int(input())
col_one = []
col_two = []
for i in range(iteration):
    color = [x for x in input().split()]
    col_one.append(color[0])
    col_two.append(color[1])
# chek if each element in col-one find in col-two
counter = int(0)
for i in range(len(col_one)):
    for j in range(len(col_two)):
        if col_one[i] == col_two[j]:
            counter += 1
print(counter)

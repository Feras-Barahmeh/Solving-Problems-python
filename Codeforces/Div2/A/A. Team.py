num_prop = int(input())
can_solution = int()
for i in range(num_prop):
    first_fre, sec_fre, ther_fre = [int(x) for x in input().split()]
    if (first_fre + sec_fre + ther_fre) >= 2:
        can_solution +=1

print(can_solution)
num_games = int(input())
count_D = count_A = 0
scuore = input()
for i in scuore:
    if i == "D":
        count_D += 1
    else:
        count_A += 1

if count_A == count_D:
    print("Friendship")
elif count_A > count_D:
    print("Anton")
elif count_D > count_A:
    print("Danik")


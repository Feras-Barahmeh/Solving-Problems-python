num_tram = int(input())
count = int(0)
temp = int(0)
while int(num_tram):
    x, y = [int(i) for i in input().split()]
    temp = int(temp+y-x)
    if temp > count:
        count = temp
    num_tram -= 1
print(count)

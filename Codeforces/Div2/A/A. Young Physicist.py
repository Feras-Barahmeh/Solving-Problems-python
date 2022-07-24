# terraple = int(input())
#
# element1 = element2 = element3 = 0
#
# for i in range(terraple):
#     number = int(input())
#     # end =  ' '
#     element1 += int(number)
#     number2 = input()
#     element2 += int(number2)
#     number3 = input()
#     element3 += int(number3)
#     print()
#
#
#
# if element1 == 0 and element2 == 0 and element3 == 0:
#     print("YES")
# else:
#     print("NO")


n = int(input())
a = [0] * 3

for i in range(n):
    b = [int(x) for x in input().split()]
    for j in range(3):
        a[j] += b[j]

ans = [x for x in a if x == 0]
print('YES' if len(ans) == 3 else 'NO')

# anather solve in down
# aADDb = input().strip()
# aADDb += ' '
# i = int(0)
# s = ''
# ls = []
# for i in aADDb:
#     if i.isspace():
#         ls.append(s)
#         s = ''
#     else:
#         s += i
# a = int(ls[0])
# b = int(ls[1])
#
# j = int(0)
# while j >= int(0):
#     a += a * 3
#     b += b * 2
#     if a >= b:
#         print(j+1)
#         break
#     j += 1

a, b = [int(x) for x in input().split()]
i = 0
while a <= b:
    a *= 3
    b *= 2
    i += 1
print(i)

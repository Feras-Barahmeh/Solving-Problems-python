# Another solution:
# n: How soldier Have Many, m: How macth bananas number buy


k, n, m = input().split()
k, n, m = int(k), int(n), int(m)

How_soldier_Have_Many = int(0)

for i in range(1, m + 1):
    How_soldier_Have_Many += i * k

if How_soldier_Have_Many - n == m:
    print(0)
else:
    if How_soldier_Have_Many - n <= 0:
        print(0)
    else:
        print(How_soldier_Have_Many - n)


# data = input().rstrip()
# fac_k = float(1)
# fac_w = float(1)
# data += ' '   # include number in list
# s_test = ''        # string for testing if char is number or not
# lis_number = []       # list include number
# for k in (data):
#     if k.isspace():
#         lis_number.append(s_test)
#         s_test = ''
#     elif k.isnumeric() or k == ".":  # check if " . " is decimal point or anther point
#         s_test += k
# k = int(0)
# for i in range(1, int(lis_number[2])+1):
#     k += int(i) * int(lis_number[0])

# if int(k - int(lis_number[1])) == lis_number[2]:
#     print(0)
# else:
#     if int(k) - int(lis_number[1]) <= 0:
#         print(0)
#     else:
#         print(int(k) - int(lis_number[1]))

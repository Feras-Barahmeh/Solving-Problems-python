# https://codeforces.com/problemset/problem/230/B
from math import sqrt, ceil
t = int(input())
nums = [int(x) for x in input().split()]
count = 2
def is_Prime(num):

    print(num)
    count_in = 2
    for j in range(3, int(num)):
        if num % j == 0:
            count_in += 1
    print(count_in)
    if count_in == 2 :
        return True
    else:
        return False

def compleat_sqrt(num):
    for ii in range(1, num//2+1):
        if sqrt(num) == ii * ii:
            return True
        # else:
        #     return False

for i in nums:
    if is_Prime(sqrt(i)) and compleat_sqrt(i):
        print("YES")
    else:
        print("NO")

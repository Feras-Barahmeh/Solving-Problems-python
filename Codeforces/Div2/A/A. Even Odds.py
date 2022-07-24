# https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

if ((n+1) // 2) >= k: # This mean we will choose from odd
    print(k * 2 - 1)
else:
    if n % 2 == 0:
        print(abs(int((2*k) - n)))
    else:
        print(abs(int((2*k) - (n+1))))

# print((n+1)/2)
# odd = []
# even = []
# for i in range(1, n+1):
#     if int(i) % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# new = odd + even
# print(new[k-1])

# result = [0] * (n+1)
# for i in range(1, len(result)):
#     if i % 2 == 0:
#         pass
#     else:
#         result[i] = i
# # result.remove(0)

# Another Answer
# count = 0
# if n / 2 >= k:
#     for i in range(1, n+1, 2):
#         count += 1
#         if k == count:
#             print(i)
#
# if int(n / 2) < k:
#     count = int(n / 2) + 1
#     for i in range(0, n+1, 2):
#         count += 1
#         if k== count :
#             print(i)
# t = n // 2
# # print(2 * k - [1, 2* t][k > t])
# print([1, 2 * t][k > t])

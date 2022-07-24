# # https://codeforces.com/problemset/problem/25/A
temp = 0
n = int(input())
ns_non = [int(x) % 2 for x in input().split()]
# print(ns_non)
for i in range(len(ns_non)):
    if ns_non.count(ns_non[i]) == 1:
        print(i+1)
        break

# for i in map(int, input().split()):
#     if temp % i != 0:
#         temp = 0
# ns = sorted(ns_non)
# print(ns)
# for i in range(len(ns)):
#     # if i+1 == len(ns):
#     #     if ns[i-1] % ns[i] != 0:
#     #         temp = ns[i]
#     #         break
#
#     if i + 1 > len(ns):
#         if ns[i+1] % ns[i] != 0:
#             temp = ns[i+1]
#             break


    # if ns_non[i] == temp:
    #     print(i+1)
    #     break
    # else:
    #     if i +1 == len(ns_non):
    #         print(1)
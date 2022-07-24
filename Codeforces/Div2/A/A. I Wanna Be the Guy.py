# https://codeforces.com/problemset/problem/469/A

n = int(input())
print('I become the guy.' if len(set(input().split()[1:] + input().split()[1:])) == n else 'Oh, my keyboard!')
# p = set(int(x) for x in input().split()[1:])
# q = set(int(y) for y in input().split()[1:])
#
# if len(q) == n or len(p) == n:
#     print("I become the guy.")
# else:
#     print("Oh, my keyboard!")

# answer
# re =[]
# for i in range(n+1):
#     if i + 1 <= len(p):
#         if p[i] not in re and p[i] != 0:
#             re.append(p[i])
#     if i + 1 <= len(q):
#         if q[i] not in re and q[i] != 0:
#             re.append(q[i])
# print(re)
# print(min(re))
# print(re)
# int(min(re)) == 1 and int(max(re)) == int(n) and
# n and (min(re) != 0 and int(max(re)) == n)

# https://codeforces.com/problemset/problem/144/A
n = int(input())
heights = [int(x) for x in input().split()]

re_max= re_min = 0
for i, e in reversed(list(enumerate(heights))):
    if int(e) == max(heights):
        re_max = i
for i, e in enumerate(heights):
    if e == min(heights):
        re_min = i

if re_max > re_min:
    print(re_max + (n-1-re_min)-1)
else:
    print(re_max + (n-1-re_min))


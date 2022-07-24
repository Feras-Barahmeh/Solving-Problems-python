# https://codeforces.com/problemset/problem/155/A

num_contests = int(input())
contests = [int(x) for x in input().split()]
counter = 0
first_contest = contests[0]
min_val, max_val = contests[0], contests[0]
for i in contests[1:]:
    if i < min_val or max_val < i:
        counter += 1

    if i < min_val:
        min_val = i

    if i > max_val:
        max_val = i
    first_contest = i
print(counter)
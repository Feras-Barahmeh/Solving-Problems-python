# https://codeforces.com/problemset/problem/228/A
si = [x for x in input().split()]
si_re = []; count = 0
for i in si:
    if i not in si_re:
        si_re.append(i)
    else:
        count += 1
print(count)
# https://codeforces.com/problemset/problem/443/A
re = []; count = 0
for i in input():
    if i not in re and i != "}" and i != "{" and i != "," and i != " ":
        re.append(i)
        count += 1
print(count)
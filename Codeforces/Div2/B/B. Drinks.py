# https://codeforces.com/problemset/problem/200/B
n = int(input()); sum = 0
pi = [float(x) for x in input().split()]
for i in range(len(pi)):
    sum += pi[i]

print("{:.12f}".format(sum/len(pi)))
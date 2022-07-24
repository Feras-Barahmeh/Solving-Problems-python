# https://codeforces.com/problemset/problem/230/A
s, n=map(int, input().split()); l = []; x=0
l = sorted(list(map(int, input().split())) for i in range(n))
for i in range(n):
    if s>l[i][0]:
        s+=l[i][1]
        x+=1
print(['NO', 'YES'][x==n])

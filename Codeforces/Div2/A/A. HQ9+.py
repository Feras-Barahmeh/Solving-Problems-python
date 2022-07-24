# https://codeforces.com/problemset/problem/133/A
p = input()
hq9 = "HQ9"
for i in p:
    if i in hq9:
        print("YES")
        exit()
print("NO")
# & AND	Sets each bit to 1 if both bits are 1
print(set("HQ9") & set(input())and"YES"or"NO")
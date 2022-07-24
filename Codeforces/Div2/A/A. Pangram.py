# https://codeforces.com/problemset/problem/520/A
input()
string = input().upper()
rep = ""
for i in range(len(string)):
    for j in range(65, 91):
        if string[i].upper() == chr(j) and string[i] not in rep:
            rep += string[i].upper()
if len(rep) >= 26:
    print("YES")
else:
    print("NO")
# Another Answer
# input()
# print(["NO", "YES"][len(set(input().lower()))==26])
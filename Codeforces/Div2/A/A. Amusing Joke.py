# https://codeforces.com/problemset/problem/141/A
# Another Solving
# print('YNEOS'[sorted(input() + input()) != sorted(input()) :: 2])
# Another Solve
string_one = input()
string_two = input()
letters = input()
all_text = string_two + string_one
all_text = "".join(all_text)
all_text = sorted(all_text)
letters = "".join(letters)
letters = sorted(letters)
print(all_text)
print(letters)
if len(all_text) > len(letters):
    print("NO")
else:
    for i in letters:
        if letters.count(i) == all_text.count(i):
            pass
        else:
            print("NO")
            exit()
    print("YES")
# Another Solve
# print('YES' if sorted(a+b)==sorted(c) else 'NO')
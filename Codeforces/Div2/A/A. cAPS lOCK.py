# https://codeforces.com/problemset/problem/131/A
string = input()
if len(string) == 1:
    print(string.swapcase())
    exit()
if string[0].islower() and string[1:].isupper():
    print(string[0].upper() + string[1:].lower())
    exit()
if string.isupper():
    print(string.swapcase())
    exit()
print(string)

# if string[0].isupper():
#     string = string
# elif string[0].islower() and string[1:].isupper():
#     string = string.swapcase()
# elif string.isupper():
#     string = string.lower()
# elif string.islower():
#     string = string.lower()
#     # exit()
# print(string)

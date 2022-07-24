# https://codeforces.com/problemset/problem/705/A
layers = int(input())
content = ["I hate", " I love"]
re = ""
for i in range(1, layers + 1):
    if i % 2 != 0: # odd
        if i > 1:
            content[0] = " I hate"
            re += content[0]
        else:
            re += content[0]

    else:
        re += content[1]

    if i != layers:
        re += " that"
    if i == layers:
        re += " it"


print(re)


# for i in range(layers):
#     if i % 3 == 0 and i != 3:
#         result.append("I hate that I love that I hate it ")
#     elif i == 3:
#         result.append("I hate that I love that I hate it ")
#
#     if i % 2 == 0 and i != 2:
#         result.append(" I hate that I love it ")
#     elif i == 2:
#         result.append(" I hate that I love it ")
#
#     if i == 1:
#         result.append("I hate it")
# print("".join(result))

# for i in range(0, layers):
#     if counter == 1:
#         result += "I hate it"
#         temp += 1
#     if counter == 2:
#         result += " I hate that I love it "
#         temp += 1
#     if counter == 3:
#         result += "I hate that I love that I hate it "
#         temp += 1
#     if counter < layers:
#         counter = temp
#     else:
#         temp = 0
#         break




n1, n2 = input(), input()
result = ""
for i in range(len(n1)):
    if n1[i] == n2[i]:
        result += '0'
    else:
        result += '1'
print(result)
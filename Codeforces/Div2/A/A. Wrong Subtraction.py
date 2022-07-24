n, k = [i for i in input().rsplit()]
new = int(0)
i = 0
while i <= int(k) - 1:
    if n[-1] == '0':
        new = int(int(n) / int(10))
        n = str(new)
    else:
        if n[-1] != '0':
            new = int(n) - 1
            # This statement by save final value
            n = str(new)
    str(n)
    i += 1
print(new)

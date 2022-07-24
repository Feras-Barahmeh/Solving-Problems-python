string = int(input())

while True:
    string = int(string)
    string += 1
    string = str(string)
    a = int(string[0])
    b = int(string[1])
    c = int(string[2])
    d = int(string[3])
    if (a != b and a!= c and a != d)and (b != a and b!=c and b != d) and \
            (c != a and c!=b and c != d) and (d != a and d!=c and d != b):
        break
print(f"{a}{b}{c}{d}")

# Another Answer
y = int(input()) + 1
while len(set(str(y)))<4: y+=1
print(y)
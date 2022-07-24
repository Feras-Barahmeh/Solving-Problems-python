number = int(input())
result = ""
for i in [4, 7, 47, 74, 744, 477]:
    if number % int(i) == int(0):
        result = "YES"
if result == "YES":
    print(result)
else:
    print("NO")

n=int(input()); print(["YES", "NO"][all(n % i for i in[4, 7, 47, 477])])
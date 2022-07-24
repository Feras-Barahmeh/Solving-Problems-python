line=int(input())
i=x=0
while i< line:
    t=input()
    if t[1] =='+':
        x=x+1
    else:
        x=x-1
    i+=1

print(x)

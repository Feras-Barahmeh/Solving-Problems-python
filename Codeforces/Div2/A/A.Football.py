n=input()
c=0
counter1=int(0)
counter0= int(0)
for i in range(len(n)):
    if n[i]=='1':
        counter1+=1
        counter0 = 0
        if counter1>=7:
            break
    if n[i] == '0':
        counter0 +=1
        counter1 = 0
        if counter0>=7:
            break
if  counter1>=7 or counter0>=7:
    print("YES")
else:
    print('NO')

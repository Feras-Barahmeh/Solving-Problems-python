string = input().lower()
var=""
for i in string:
    if i in string:
        if i in var:
            pass
        else:
            var=var+i



if len(var)%2==0:
    print("CHAT WITH HER!")
else:
    print('IGNORE HIM!')

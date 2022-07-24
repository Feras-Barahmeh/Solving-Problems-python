string=input()
counter_upper=int(0)
counter_lower = int(0)
for i in string:
    if i.islower():
        counter_lower+=1
    elif i.isupper():
        counter_upper+=1
if counter_lower == counter_upper:
    print(string.lower())
elif counter_upper>counter_lower:
    print(string.upper())
elif counter_lower>counter_upper:
    print(string.lower())
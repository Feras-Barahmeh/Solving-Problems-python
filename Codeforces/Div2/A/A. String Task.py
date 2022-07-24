string =input()
string=string.lower()
litter = ['a', 'e', 'i', 'u', 'o', 'y']    # ِِA, I, E O,U)
finel_value= ''
for counter in range(0,len(string)):
    if string[counter] not in litter:
        finel_value+= '.'
        finel_value+=string[counter]
print(finel_value)
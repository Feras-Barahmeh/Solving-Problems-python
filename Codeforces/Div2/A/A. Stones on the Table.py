# x=int(input())
# string=input()
# list=[]
# counter=0
# for i in range(0,x):
#     list.append(string[i])
# list.append(" ")
# list.append(" ")
# n_str=''.join(list)
# o=int(0)
# for j in range (len(n_str)-2):
#     if n_str[o]==n_str[o+1]:
#         counter+=1
#     o+=1
# print(counter)


# Another Solution
num_sto = int(input())
colors = input()
counter = int(0)
colors += ""
for key in range(len(colors) - 1):
    if key != len(colors):
        if colors[key] == colors[key + 1]:
            counter += 1
print(counter)
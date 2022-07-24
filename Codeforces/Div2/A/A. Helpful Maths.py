# string = input()
# s=''
# for i in string:
#     if i=='+':
#         pass
#     else:
#         s+=i
# one = two = three =''
# for j in s :
#     if j =="1":
#         one +="1"
#     elif j =="2":
#         two += "2"
#     elif j == "3" :
#         three+=j
# all_number = one+two+three
# all_number_new =''
# for k in range (0,len(all_number)):
#     all_number_new += all_number[k]+"+"
# print(all_number_new.rstrip(all_number_new[-1]))

# Git Hup code
# s = input()
# n1 = n2 = n3 = 0
# for i in range(0, len(s), 2):
#     if s[i] == '1':
#         n1 += 1
#     elif s[i] == '2':
#         n2 += 1
#     else:
#         n3 += 1
# ss = "1+" * n1 + "2+" * n2 + "3+" * n3
# print(ss[:-1])


# Anther code
# string = input()
# active_string = string.split("+")
# active_string.sort()
# active_string = "".join(active_string)
#
# ne_str = ""
# for i in str(active_string):
#     ne_str += i
#     ne_str += "+"
# list(ne_str).pop()
# print(ne_str[0:len(ne_str) - 1])
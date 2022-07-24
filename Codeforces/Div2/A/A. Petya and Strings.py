string_one = input().lower()
string_two = input().lower()


counter = 0
for i in range(len(string_one)):
    if string_one[i] == string_two[i]:
        counter += 1
        if counter == len(string_one) or counter == len(string_two):
            print(0)
            break
    else:
        if ord(string_one[i]) > ord(string_two[i]):
            print(1)
            break
        if ord(string_one[i]) < ord(string_two[i]):
            print(-1)
            break

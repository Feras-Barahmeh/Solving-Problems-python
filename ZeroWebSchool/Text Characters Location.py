string = input()
letter_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_lower = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(string)):
    if string[i].isupper():
        # Can not use find method, you can using for loop looping in letter upper variable,
        # and using counter using this for find position in letter upper.
        print(letter_upper.find(string[i])+1,end=" ")
    if string[i].islower():
        print(letter_lower.find(string[i])+1,end=" ")
# you can using anther algorithm the first check if upper upper swap it lower  and remove letter upper variable
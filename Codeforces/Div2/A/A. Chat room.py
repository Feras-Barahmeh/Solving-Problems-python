say_hello = input()
key = 'hello'
pointer  = 0

for i in range(len(say_hello)):
    if say_hello[i] == key[pointer] :
        pointer += 1
    if  pointer >= len(key):
        break
if pointer == len(key):
    print("YES")
else:
    print("NO")
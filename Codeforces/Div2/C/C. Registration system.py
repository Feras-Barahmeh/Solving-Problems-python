# def is_found(names, requirement_name):
#     count = 0
#     for i in names:
#         if i == requirement_name:
#             count += 1
#     if count <= 1:
#         return
#     else:
#         return count

# num_names = int(input())
# db = []
# for _ in range(num_names):
#     name = input()
#     if name in db:
#         db.append(name)
#         print(f"{name}{is_found(db, name)-1}")
#     else:
#         db.append(name)
#         print("OK")
n=int(input())
d={}

for i in range(n):
        s=input()
        if s in d:
            print(s+str(d[s]))
            d[s] += 1
            # print(d)
        else:
            print("OK")
            d[s] = 1
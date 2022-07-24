# https://codeforces.com/contest/1634/problem/A
num_iter = int(input())

counter = 0
s_list = []
result_lis = []
for i in range(num_iter):
    n, k = map(int, input().split())
    s = str(input())
    # if k == 0 or k == 1:
    #     print(1)
    # else:
    for j in range(k):
        s1 = [x for x in s]
        s1.reverse()
        result = "".join(s1) + s
        result2 = s + "".join(s1)
        if result not in result_lis:
            result_lis.append(result)
            counter += 1
        elif result2 not in result_lis:
            result_lis.append(result2)
            counter += 1
    print(counter)

# 3 2
# aab
# 7 1
# abacaba
# 2 0
# ab
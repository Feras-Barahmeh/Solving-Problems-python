queue_len, second = map(int, input().split())
queue_ele = input()
queue_ele = [x for x in queue_ele]
skip = False
for t in range(second):
    for ele in range(len(queue_ele) - 1):
        if skip:
            skip = False
            continue
        if queue_ele[ele] == 'B' and queue_ele[ele + 1] == 'G':
            queue_ele[ele] = 'G'
            queue_ele[ele + 1] = 'B'
            skip = True
    skip = False


print("".join(queue_ele))

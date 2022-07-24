num_coins = int(input())
sequence = [int(x) for x in input().split()]
sequence = sorted(sequence, reverse=True)
summation = counter = 0
for i in range(len(sequence)):
    summation += int(sequence[i])
    counter += 1
    if summation > sum(sequence[i+1:]):
        print(counter)
        break

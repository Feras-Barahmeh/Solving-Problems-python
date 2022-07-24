input()
count_one, count_two, count_three, count_four = map(input().count, ('1', '2', '3', '4'))

summation = count_four + count_three

if count_one > count_three:
    summation += (count_two * 2 + (count_one - count_three) + 3) // 4
else:
    summation += (count_two * 2 + 3) // 4
print(summation)
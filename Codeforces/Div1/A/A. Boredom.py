# def most_frequent(List):
#     counter = 0
#     num = List[0]
#     for i in List:
#         curr_frequency = List.count(i)
#         if curr_frequency > counter:
#             counter = curr_frequency
#             num = i
#     return num
# # 9
# # 1 2 1 3 2 2 2 2 3
#
#
# iter_num = int(input())
# sequence = [x for x in input().split()]
#
#
# frequence_value = int(most_frequent(sequence))
# frequence_num = sequence.count(str(frequence_value))
#
# less_num = int(sequence.count(str(int(frequence_value) - 1)))
# less_value = int(frequence_value - 1)
#
# great_num = int(sequence.count(str(int(frequence_value) + 1)))
# great_value = int(frequence_value + 1)
#
#
# # step =
# result = []
# for ii in range(len(sequence)):
#     if int(sequence[ii]) == less_value or int(sequence[ii]) == great_value:
#         pass
#     else:
#         result.append(sequence[ii])
#     if frequence_num == less_num == great_num:
#         pass


input()
sequence = [0] * 10 # Each position is pointer to value which included.
for value in map(int, input().split()):
    sequence[value] += value

temp1 = temp2 = result = 0
for i in sequence:
    result = temp1
    temp1 = max(result, temp2 + i)
    temp2 = result

# i = 0
# result = 1
# temp = 2

# print(sequence)
print(result)
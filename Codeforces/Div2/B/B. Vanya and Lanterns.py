number_of_lanterns, length_street = input().split()
position_lanterns = [int(x) for x in input().split()]
position_lanterns.sort()
# Find The Largest space between lanterns This value initial value radius.
max_dalta = float(0)
first = ""
second = ""
for element in range(len(position_lanterns)):
    if position_lanterns[element] != position_lanterns[
            -1]:  # This statement for pass error " IndexError: list index out of range "
        if position_lanterns[element + 1] - position_lanterns[element] > max_dalta:
            max_dalta = position_lanterns[element +
                                          1] - position_lanterns[element]
            first = str(position_lanterns[element + 1])
            second = str(position_lanterns[element])
radius = float(max_dalta / 2.00000000)
t = float(radius)
if position_lanterns[0] == 0 and position_lanterns[-1] == int(length_street):
    print("{:.10f}".format(radius))
    quit()
else:

    if position_lanterns[0] != 0:
        if position_lanterns[0] > t:
            radius = position_lanterns[0]
        else:
            radius = t

    if position_lanterns[-1] != int(length_street):
        if abs(float(length_street) - position_lanterns[-1]) > t:
            radius = int(length_street) - position_lanterns[-1]

    if position_lanterns[-1] != float(length_street) and position_lanterns[0] != 0:
        three = [position_lanterns[0], abs(
            float(length_street) - position_lanterns[-1]), t]
        radius = max(three)

print("{:.10f}".format(radius))

# 7 15
# 0 3 5 7 9 14 15

# 2 5
# 2 5


# 46 615683844
# 431749087 271781274 274974690 324606253 480870261 401650581 13285442 478090364 266585394 425024433 588791449 492057200 391293435 563090494 317950 173675329 473068378 356306865 311731938 192959832 321180686 141984626 578985584 512026637 175885185 590844074 47103801 212211134 330150 509886963 565955809 315640375 612907074 500474373 524310737 568681652 315339618 478782781 518873818 271322031 74600969 539099112 85129347 222068995 106014720 77282307

#  == > 22258199.5000000000

# 2 555
# 200 300
#  ===> 255

# 1 1
# 0
# ==> 1.0000000000

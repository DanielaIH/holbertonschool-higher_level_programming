#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    sum_1 = 0
    for i in range(len(my_list)):
        if my_list[i] not in new:
            sum_1 += my_list[i]
            new.append(my_list[i])
    return sum_1

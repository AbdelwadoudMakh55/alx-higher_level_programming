#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wei_score = 0
    weights_sum = 0
    for score in my_list:
        wei_score += score[0] * score[1]
        weights_sum += score[1]
    return wei_score / weights_sum

#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return(None)
    if my_list:
        max_n = my_list[0]
        for i in my_list:
            if i > max_n:
                max_n = i
        return(max_n)

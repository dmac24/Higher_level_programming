#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")

        except:
            break
        printed += 1
    print()
    return printed

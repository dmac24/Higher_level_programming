#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    length = len(argv) - 1
    add = 0

    if length == 0:
        print("{}".format(add))

    else:
        for args in argv[1:]:
            add += int(args)
        print("{}".format(add))

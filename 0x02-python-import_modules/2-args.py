#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1

    if length == 0:
        print("{} arguments.".format(length))

    else:
        if length == 1:
            print("{} argument:".format(length))

        else:
            print("{} arguments:".format(length))

        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))

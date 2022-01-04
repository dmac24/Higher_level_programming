#!/usr/bin/python3
for i in range(0, 9):
    if i < 8:
        for j in range(i + 1, 10):
            print("{:d}{:d}".format(i, j), end=', ')
    else:
        print("{:d}{:d}".format(i, j))

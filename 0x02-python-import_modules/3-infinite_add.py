#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from sys import argv
    sum = 0
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        sum += int(sys.argv[i])
    print("{:d}".format(sum))
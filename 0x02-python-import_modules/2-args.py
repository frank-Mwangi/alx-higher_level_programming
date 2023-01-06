#!/usr/bin/python3
def args(argv):
    n = len(argv) - 1
    if n == 0:
        print("{} argument.".format(n))
        return
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))
    i = 1
    while 1 < n:
        print("{}: {}".format(i, argv[i]))
        i += 1
if __name__ == "__main__":
    import sys
    args(sys.argv)

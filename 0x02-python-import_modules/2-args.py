#!/usr/bin/python3
def args(argv):
    n = len(argv) - 1
    if n == 0:
        print("{:d} argument.".format(n))
        return
    else:
        if n == 1:
            print("{:d} argument:".format(n))
        else:
            print("{:d} arguments:".format(n))
        i = 1
        while 1 <= n:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1


if __name__ == "__main__":
    import sys
    args(sys.argv)

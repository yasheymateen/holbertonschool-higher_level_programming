#!/usr/bin/python3
if __name__ == "__main__":
    import add_0
    a = 1
    b = 2
    from add_0 import add
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

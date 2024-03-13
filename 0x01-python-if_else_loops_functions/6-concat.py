#!/usr/bin/python3
for a in range(0, 10):
    b = a + 1
    while (b <= 9):
        if (a == 8 and b == 9):
            print("{}{}".format(a, b))
        else:
            print("{}{}".format(a, b), end=", ")
        b += 1

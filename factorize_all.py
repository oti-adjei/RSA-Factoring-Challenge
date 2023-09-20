#!/usr/bin/env /usr/bin/python3

def factorize_all(line):
    if line <= 1:
        return None, None
    if line % 2 == 0:
        print("{}={}*{}".format(line, line // 2, 2))
        return line // 2, 2
    else:
        for i in range(3, line // 2, 2):
            if line % i == 0:
                    print("{}={}*{}".format(line, line // i, i))
                    return line // i, i
    return None, None

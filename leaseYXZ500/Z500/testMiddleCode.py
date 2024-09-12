
from random import choice

import random

def MiddleCodeQuery():
    list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PCC_wi = [1, 3, 5, 7, 11, 2, 13, 1, 1, 17, 19, 97, 23, 29];
    d = random.randint(1, 99)
    while True:
        sum = 0
        code = []
        for i in range(14):
            a = choice(list)
            code.append(a)
            c = list.index(a)
            b = PCC_wi[i]
            sum += b * c
        res = sum % 97 + 1
        if res == d:
            break;
    if d < 10:

        print(''.join(code) + '0' + str(d))
    else:

        print(''.join(code) + str(d))

if __name__ == '__main__':
    MiddleCodeQuery()


#!/usr/bin/env python

with open('luck.txt', 'r') as f:
    while True:
        nums = []
        line = f.readline()
        if not line:
            break

        a, desc, luck = line.split()
        a = int(a)
        print '%s, %d (%s)' % (desc, a, luck)
        for x in range(1, 10000):
            y = x / 80.0
            z = int(y)
            if y > z:
                if ((y - z) * 80) == a:
                    nums.append(x)
            elif y <= 1:
                if (y * 80) == a:
                    nums.append(x)
        print ', '.join([('%4s' % n) for n in nums])
        print

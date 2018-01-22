# -*- coding: utf-8 -*-

import itertools


def pi(N):
    s = [0]
    numbers = itertools.count(1, 2)
    m = itertools.takewhile(lambda x: (x + 1) / 2 <= N, numbers)
    n = [(-1) ** ((x + 1) / 2 - 1) * x for x in m]
    for i in n:
        s[0] = s[0] + 4 / i
    return s[0]

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
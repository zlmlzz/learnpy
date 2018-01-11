# -*- coding: utf-8 -*-

import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        r = fn(*args, **kwargs)
        t_end = time.time()
        result = t_end - t_start
        print('%s executed in %s ms' % (fn.__name__, result))
        return r
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

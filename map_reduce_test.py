# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    index = s.index('.')
    integer = reduce(lambda x, y: x * 10 + y, map(int, s[:index]))
    decimal = reduce(lambda x, y: x / 10 + y, map(int, s[index + 1:][::-1])) / 10
    return integer + decimal

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

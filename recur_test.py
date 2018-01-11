# -*- coding: utf-8 -*-

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        # n-1个a 移动到b上
        move(n - 1, a, c, b)
        # 1个a移动到c上
        move(1, a, b, c)
        # n-1个b移动到c上
        move(n - 1, b, a, c)

move(3, 'A', 'B', 'C')

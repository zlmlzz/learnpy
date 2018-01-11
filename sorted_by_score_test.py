# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_score(t):
    return t[1]

# 这边我自己加了一个参数，不加的话我还没想到
L2 = sorted(L, key=by_score, reverse=True)
print(L2)
# -*- coding: utf-8 -*-

import os


def search(path, word):
    l = os.getcwd()
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        if os.path.isfile(fp) and word in filename:
            print(os.path.split(fp)[0][len(l):] + '\t\t\t' + filename)
        elif os.path.isdir(fp):
            search(fp, word)


P = input('搜索的路径:')
S = input('要搜索的内容：')
search(P, S)




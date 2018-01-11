# -*- coding: utf-8 -*-

import os, time

def get_size(filename):
    return str(os.path.getsize(filename))

def is_file(filename):
    if os.path.isdir(filename):
        return 'DIR'
    else:
        return ''

def ctime(filename):
    return time.ctime(os.path.getctime(filename))


f = os.listdir('.')
for filename in f:
    print(ctime(filename) + '\t' + is_file(filename) + '\t' + get_size(filename) + '\t' + filename)




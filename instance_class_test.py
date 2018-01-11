# -*- coding: utf-8 -*-

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        setattr(Student, 'count', Student.count + 1)




# 测试:
if Student.count != 0:
    print(Student.count)
else:
    bart = Student('Bart')
    if Student.count != 1:
        print(bart.count)
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

# -*- coding: utf-8 -*-

# 闭包
# 当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
def count1():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count1()
print f1(), f2(), f3()


def count2():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print f1(), f2(), f3()


def count3():
    fs = []
    for i in range(1, 4):
        fs.append(lambda: i * i)
    return fs

f1, f2, f3 = count3()
print f1(), f2(), f3()


def count4():
    fs = []
    for i in range(1, 4):
        def f(j):
            return lambda: j * j
        fs.append(f(i))
    return fs

f1, f2, f3 = count4()
print f1(), f2(), f3()
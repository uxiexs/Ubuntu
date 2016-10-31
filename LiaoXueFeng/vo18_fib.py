#/usr/bin/python3
# coding:utf-8


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    print('down')

def fibPrint(max):
    for n in fib(max):
        print(n)

fibPrint(20)

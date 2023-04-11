a = 0
b = 2
L = [1, 2]

try:
    c = b/a
except ZeroDivisionError:
    print('division by zero')

try:
    print(d)
except NameError:
    print('not defined value')

try:
    print(L[3])
except IndexError:
    print('out of range of "L"')
from functools import reduce

def str2float(s):
    strflo = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '.': -1
    }
    frac = 0

    def flt(x,y):
        nonlocal frac   # using global variable
        if frac == 0:
            if x == -1:
                frac += 2  # matching the following frac += 1
                return y * 0.1
            if y == -1:
                frac += 1
                return x
            else:
                return x * 10 + y
        else:
            frac += 1
            return x + y * 0.1 ** (frac - 1)

    def str2num(s):
        return strflo[s]
    
    return reduce(flt, map(str2num, s))

# test
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

# stricter test
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
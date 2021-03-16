import numpy as np
from decimal import getcontext, Decimal as D
#from tabulate import tabulate


def metoda_newtona(f, df, x0, n, d):
    """
    oblicza max. n iteracji metody Newtona dla funkcji f o pochodnej df
    z punktem startowym x0. Zatrzymuje się jeżeli |f(x_k)| < d.
    """
    x = np.zeros(shape=(n,))
    x[0] = x0
    y = f(x0)
    k = 0
    while (k < n - 1) and (np.abs(y) > d):
        x[k + 1] = x[k] - f(x[k]) / df(x[k])
        k += 1
        y = f(x[k])
    return x[:k]


def f(x):
    return x * (x ** 9 - 1) - 1


def df(x):
    return 10 * x ** 9 - 1


#print(metoda_newtona(f, df, 2, 5, 0.001))


def p1_metoda_newtona(f, df, x01, x02):
    x1 = []
    x2 = []
    k = 0
    x1.append(x01)
    x2.append(x02)
    m = (x1[0] + x2[0]) / 2
    for k in range(10):
        if df(x1[k]) < df(x1[0]):
            l1 = df(x1[0])
        else:
            l1 = df(x1[k])
        if df(x2[k]) > df(x2[0]):
            l2 = df(x2[0])
        else:
            l2 = df(x2[k])
        x1.append(m - f(m) / l1)
        x2.append(m - f(m) / l2)
        if f(m) >= 0:
            if x1[k] > x1[k + 1]:
                x1[k + 1] = x1[k]
        else:
            if x2[k] < x2[k + 1]:
                x2[k + 1] = x2[k]
        if x1[k+1] > x2[k+1]:
            x1[k+1], x2[k+1] = x2[k+1], x1[k+1]
        k += 1
        m = (x1[k] + x2[k]) / 2
    '''results = [x1[:k], x2[:k]]
    print(tabulate(results))'''
    for i in range(10):
        print(str(x1[i]) + '   ' + str(x2[i]) + '\n')
    return (x1[k] + x2[k]) / 2

getcontext().prec = 13
#print(p1_metoda_newtona(f, df, D('1.0'), D('1.5')))

'''
def p2_metoda_newtona(f, df, x01, x02):
    x1 = np.zeros(1000)
    x2 = np.zeros(1000)
    x1[0] = x01
    x2[0] = x02
    m = (x01 + x02) / 2
    k = 0
    while round(x2[k], 2) != round(x1[k], 2):
        x1[k + 1] = m - f(m) / df(x1[k])
        x2[k + 1] = m - f(m) / df(x2[k])
        if f(m) >= 0:
            if x1[k] > x1[k + 1]:
                x1[k + 1] = x1[k]
        else:
            if x2[k] < x2[k + 1]:
                x2[k + 1] = x2[k]
        k += 1
        m = (x1[k] + x2[k]) / 2
    print(x1[:k])
    print(x2[:k])
    return (x1[k] + x2[k]) / 2
'''


def p3_metoda_newtona(f, df, x01, x02):
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    k = 0
    x1.append(x01)
    x2.append(x02)
    m = (x1[0] + x2[0]) / 2
    for k in range(10):
        '''if df(x1[k]) < df(x1[0]):
            l1 = df(x1[0])
        else:
            l1 = df(x1[k])
        if df(x2[k]) > df(x2[0]):
            l2 = df(x2[0])
        else:
            l2 = df(x2[k])
        x1.append(m - f(m) / l1)
        x2.append(m - f(m) / l2)
        k += 1
        m = (x1[k] + x2[k]) / 2'''
        if df(x1[k]) < df(x1[0]):
            l1 = df(x1[0])
        else:
            l1 = df(x1[k])
        if df(x2[k]) > df(x2[0]):
            l2 = df(x2[0])
        else:
            l2 = df(x2[k])
        x1.append(m - f(m) / l1)
        x2.append(m - f(m) / l2)
        if f(m) >= 0:
            if x1[k] > x1[k + 1]:
                x1[k + 1] = x1[k]
        else:
            if x2[k] < x2[k + 1]:
                x2[k + 1] = x2[k]
        if x1[k+1] > x2[k+1]:
            x1[k+1], x2[k+1] = x2[k+1], x1[k+1]
        k += 1
        m = (x1[k] + x2[k]) / 2
        if f(m) > 0:
            y1.append(x1[k])
            y2.append(m)
        elif f(m) < 0:
            y1.append(m)
            y2.append(x2[k])
        else:
            y1.append(x1[k])
            y2.append(x2[k])
    '''results = [x1[:k], x2[:k]]
    print(tabulate(results))'''
    for i in range(10):
        print(str(y1[i]) + '   ' + str(y2[i]) + '\n')
    return (y1[k-1] + y2[k-1]) / 2

getcontext().prec = 13
print(p3_metoda_newtona(f, df, D('1.0'), D('1.5')))
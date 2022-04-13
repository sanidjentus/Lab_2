from numpy import arange
from scipy.integrate import solve_ivp
from sympy import *


def mathematical_expectation():
    t0 = 0
    t1 = 1
    tau = 0.25
    N = int((t1 - t0) / tau)
    h = 0.1
    x0 = 1
    x1 = 0
    valueT = Symbol('t')
    q = (1 + valueT) ** (-2)
    print(q)
    valueU = Symbol('u')
    f = 1 - 2 * valueU
    print(f)
    fu = []
    for m in range(0, N - 1):
        fu.append(f.subs(valueU, (m * h)))
    print("f(u): ", fu)
    p = 1/N
    M0 = x0
    M1 = x1
    Yn0 = []
    Yn1 = []
    for m in range(0, N-1):
        Yn0.append(M0 * fu[m])
        Yn1.append(tau * M1 * fu[m])
    print("Yn0: ", Yn0)
    print("Yn1: ", Yn1)
    Yn = []
    Yn.append(Yn0)
    Yn.append(Yn1)
    print("Yn: ", Yn)

    k = 2
    for n in range(0, N - 2):
        Ytmp = []
        qt = q.subs(valueT, (t0 + n * tau))
        for m in range(0, N - k):
            tmp = (2 - tau/h) * Yn[n+1][m] + (tau/h) * (Yn[n+1][m+1] - Yn[n][m+1]) + ((tau/h) - 1 - qt ** 2)
            Ytmp.append(tmp)
        Yn.append(Ytmp)
        k = k + 1

    print("Yn: ", Yn)
    return 0


mathematical_expectation()
from constants.globalMethods import *
import math as math

xnFuction = lambda x: x - (fFuction(x) / derivativeFuction(x))

def newtonMethod(A: float, B: float, K: int):
    xo = gradient(A, B)
    xn = xo
    for i in range(0, K):
        xn = xnFuction(xn)
        print(f"X_{i + 1} = {xn}")


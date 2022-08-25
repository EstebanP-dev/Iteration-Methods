from webbrowser import Grail
from constants.globalMethods import *
import math as math

def bisectionMethod(A: float, B: float, K: int):
    a = A
    b = B

    for i in range(0, K):
        mn = gradient(a, b)
        fa = fFuction(a)
        fb = fFuction(b)
        fmn = fFuction(mn)

        if(a * b < 0):
            break

        print(f"X_{i + 1}: [{a} ; {b}]")
        
        if(fa * fmn < 0):
            b = mn
            continue
        
        if(fb * fmn < 0):
            a = mn
            continue

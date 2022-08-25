from constants.globalMethods import *
import fuctions.bisection as bs
import fuctions.newton as nw


A = 2
B = 2.5
E = 10**-5 #ERROR
iterations = iterationsFunction(A, B, E)
#K = 5 #NUMERO DE ITERACIONES
K = round(iterations) 


print("=========== BISECCIÓN ===========")
bs.bisectionMethod(A, B, K)
print("=========== NEWTON ===========")
nw.newtonMethod(A, B, K)
print("=========== END ===========")

print(f"Iteraciones necesarios para {E}: {K} aproximadamente")
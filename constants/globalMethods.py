import math as math

fFuction = lambda x: (x**2) - x - math.cos(x) - 3
derivativeFuction = lambda x: 2*x + math.sin(x) - 1
gradient = lambda a,b: (a + b) / 2
iterationsFunction = lambda a, b, e: (math.log((b - a) / e)) / (math.log(2))
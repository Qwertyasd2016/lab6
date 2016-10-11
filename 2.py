import random

random.seed(0)
n = 10000000
x = [random.uniform(-2, 2) for i in range(n)]
f = [-1*x[i]*x[i] + 4 for i in range(len(x))]
integral = (sum(f)*4)/n
print(integral)
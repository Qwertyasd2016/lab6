import random

random.seed(0)
n = 10000000
x = [random.uniform(-3, 3) for i in range(n)]
f = []
for i in range(len(x)):
    if -2<x[i]<2:
        f.append(-x[i]*x[i]+4)
integral = (sum(f)*6)/n
print(integral)
import random
import matplotlib.pyplot as plt

random.seed(0)
n = 10000000
x = [random.uniform(-3, 3) for i in range(n)]
f = [-1*x[i]*x[i] + 4 for i in range(len(x))]
integral = (sum(f)*6)/n
print(integral)
plt.show()
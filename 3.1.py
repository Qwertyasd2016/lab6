import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import random
def get_percentile(values, n):
    p = [np.percentile(values, 100*i/n) for i in range(n)]
    p[0] = 0.0
    return p
def get_percentile_number(v, p):
    x = 0
    for i in range(len(p)):
        if v >= p[i]:
            x = i
    return(x)
def value_equalization(value, percentiles, add_random):
    idx = get_percentile_number(value, percentiles)
    if add_random:
        random_noise = random.uniform(0, percentiles[idx]/4)
        new_value = percentiles[idx] + random_noise
    else:
        new_value = percentiles[idx]
    return new_value
def values_equalization(values, percentiles, add_random):
    for i in range(len(values())):
        if add_random:
            values[i] = value_equalization(values[i], percentiles, add_random = True)
        else:
            values[i] = value_equalization(values[i], percentiles, add_random = False)
    return values
arr = []
with open('img.txt', 'r') as f:
    for line in f:
        values = line.rstrip().split(' ')
        arr.append(values)
data = np.array(arr).astype(float)
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.show()
new_data = data.flatten()
plt.hist(new_data, bins=10)
plt.show()
percentiles = get_percentile(new_data, 10000)
new_data = values_equalization(new_data, percentiles, add_random = False)
plt.hist(new_data, bins=10)
new_data = new_data.reshape((200, 267))
plt.imshow(new_data, cmap = plt.get_cmap('gray'))
#data = np.array(arr).astype(float)
#percentiles = get_percentile(data, 10)
#new_img = data.flatten()
#print(new_img)
#new_data = values_equalization(new_img, percentiles, add_random = False)
#print(new_data)
#new_img = new_data.reshape((200, 267))
#plt.imshow(new_img, cmap = plt.get_cmap('gray'))
#plt.show()
#print(new_img)
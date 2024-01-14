import numpy as np
import matplotlib.pyplot as plt
features = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])
w = [0, 0]
bias = 0
learning_rate = 0.1
epoch = 30
for j in range(0, epoch):
    print("epoch ", j)
    global_delta = 0
    for i in range(0, features.shape[0]):
        actual = labels[i]
        instance = features[i]

        x0 = instance[0]
        x1 = instance[1]

        sum_unit = x0 * w[0] + x1 * w[1] + bias

        if sum_unit > 0:
            fire = 1
        else:
            fire = 0
        
        delta = actual - fire
        global_delta = global_delta + abs(delta)

        print("prediction:", fire, " whereas actual was ", actual," (error:", delta,")")

        w[0] = w[0] + delta * learning_rate * x0
        w[1] = w[1] + delta * learning_rate * x1

        bias = bias + (delta * learning_rate)
    print("------------------")
    print(w[0], w[1])
    print(bias)

    if global_delta == 0:
        break

x_vals = np.linspace(-0.2, 1.2, 100)
y_vals = (-bias - w[0] * x_vals) / w[1]

plt.plot(x_vals, y_vals, label='Decision Boundary')
plt.scatter(features[:, 0], features[:, 1], c=labels, cmap=plt.cm.Paired, edgecolors='k', marker='o', s=100, label='Data Points')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.show()
import numpy as np

features = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])
w = np.array([0.1, 0.1])  # Use NumPy array for weights
bias = 10
learning_rate = 0.3
epoch = 100

for j in range(epoch):
    print("epoch ", j)
    global_delta = 0

    for i in range(features.shape[0]):
        actual = labels[i]
        instance = features[i]

        x0, x1 = instance  # Unpack the instance directly

        sum_unit = np.dot(instance, w) - bias  # Use dot product for weighted sum

        if sum_unit > 0:
            fire = 1
        else:
            fire = 0

        delta = actual - fire
        global_delta += abs(delta)

        print("prediction:", fire, " whereas actual was ", actual, " (error:", delta, ")")

        w += delta * learning_rate * instance  # Update weights
        bias += delta * learning_rate  # Update bias

    print("------------------")
    print("Weights:", w)
    print("Bias:", bias)

    if global_delta == 0:
        break
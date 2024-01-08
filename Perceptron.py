from data import get_mnist
import numpy as np
import matplotlib.pyplot as plt

images, labels = get_mnist()
w_i_h = np.random.uniform(-0.5, 0.5, (20, 784))
w_h_o = np.random.uniform(-0.5, 0.5, (10,20))
b_i_h = np.zeros((20,1))
b_h_o = np.zeros((20,1))

learn_rate = 0.01 
nr_correct = 0
epochs = 3
for epoch in range(epochs):
    for img, l in zip(images, labels):
        img.shape += (1,)
        l.shape += (1,)
        h_pre = b_i_h + w_i_h @ img
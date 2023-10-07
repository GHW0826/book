import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 1.0)
y = relu(x)
print(y) # [0.26894142 0.73105858 0.88079708]

plt.plot(x, y)
plt.ylim(-0.1, 5.1) # y축 범위 지정
plt.show()
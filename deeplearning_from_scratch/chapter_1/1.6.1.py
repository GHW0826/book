print()

import numpy as np
import matplotlib.pyplot as plt

# 1.6.1
x = np.arange(0, 6, 0.1) # 0 ~ 6까지 0.1 간격으로 생성
y = np.sin(x)

plt.plot(x, y)
plt.show()

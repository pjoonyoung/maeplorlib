import numpy as np
import matplotlib.pyplot as plt

arr = np.random.standard_normal((30,40))

plt.matshow(arr)
plt.colorbar(shrink=0.8,aspect=10)
plt.show()
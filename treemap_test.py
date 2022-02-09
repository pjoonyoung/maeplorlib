import matplotlib.pyplot as plt
import squarify

size = [40,30,20,10]


labels = ['apple','orange','banana','grape']
color = ['red','blue','green','yellow']

squarify.plot(size,10,10,label=labels,color=color)

plt.show()
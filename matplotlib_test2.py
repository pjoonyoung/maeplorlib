import matplotlib.pyplot as plt
import numpy as np

data = np.arange(0,2,0.2)
print(data)

# plt.plot(data, data, 'r--' ,data,data**2, 'b-' ,data,data**3, 'g:')
plt.plot(data, data, color="#FF00DD", marker="^", markersize=10)
plt.plot(data, data**2, color="lightgray", linewidth=3)
plt.plot(data, data**3, 'g:')
plt.grid(True, axis='y', linestyle=":", alpha=0.5)
plt.xticks([0,1,2], labels=['JAN','FEB','MAR'])
plt.yticks([1,2,3,4,5], labels=['100k','200k','300k','400k','500k'])
plt.tick_params(axis='both',direction="in",length=100,pad=20,labelsize=15)
title_font = {'fontsize':20, 'fontweight':'bold'}
plt.title('Sample Graph Title', fontdict= title_font,loc='right',pad=20)

plt.show()
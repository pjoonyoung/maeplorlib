import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (10,8)
plt.rcParams['font.size'] = 15

x = np.arange(0,3)
y1 = x + 1
y2 = -x - 1

fig,ax1 = plt.subplots()
line1 = ax1.plot(x,y1,'red',label='weight')
ax1.set_xlabel('weight')
ax1.set_ylabel('height')


ax2 = ax1.twinx() # ax1과 x축을 공유하는 새로운 객체 ax2 생성
line2 = ax2.plot(x,y2,'blue',label='height')
ax2.set_ylabel('age')

ax_legend = line1 + line2
labels = [i.get_label()for i in ax_legend] # labels = [label1, label2]
ax1.legend(ax_legend,labels)

plt.show()
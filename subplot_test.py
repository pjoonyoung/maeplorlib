import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
x2 = [3,4,5,6,7]

y1 = [2,4,6,8,10]
y2 = [3,6,9,12,15]

# plt.subplot(2,1,1)
plt.subplot(1,2,1)
plt.plot(x1,x2)
plt.title('1st Graph')

# plt.subplot(2,1,2)
plt.subplot(1,2,2)
plt.plot(y1,y2)
plt.title('2nd Graph')

plt.tight_layout()

plt.show()
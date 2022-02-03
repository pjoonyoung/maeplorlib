import matplotlib.pyplot as plt


# plt.plot([1,2,3,4],[5,6,7,8], linestyle=":", marker="o", color="#B70000")
x =[1,2,3,4]
y =[5,6,7,8]
plt.plot(x,y)

plt.xlabel('X-LABEL')
plt.ylabel('Y-LABEL')
# plt.axis([0,10,0,15])
# plt.fill_betweenx(x[1:3],y[1:3],color="#B70000",alpha=0.5)
plt.fill([1.5,1.5,3.5,3.5],[2.5,4.5,2.5,4.5],color="pink")
plt.show()
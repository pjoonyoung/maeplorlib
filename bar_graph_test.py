import matplotlib.pyplot as plt

x = [0,1,2]
data = [100,200,300]
year = ['2019','2020','2021'] #축 눈금레이블(xtick)
# plt.bar(x, data, width=0.5,color='pink',edgecolor='red',linewidth=3,align='edge')
# plt.xticks(x, year)

plt.style.use('ggplot')

plt.barh(x, data, height=0.5, color='green', tick_label=year)
plt.show()
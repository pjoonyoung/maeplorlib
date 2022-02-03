import matplotlib.pyplot as plt
import numpy as np

# weight = [68,71,62,77,80,71,62,68,77,65,69,78,77,68,75,76,69,66,65,64,63,71,73,80,74,78]
# plt.hist(weight)
# plt.show()

data1 = np.random.randn(10000) # 표준 정규분포의 임의의 데이터 10000개 추출

font1 = {'family':'Arial',
         'color':'red',
         'size':15,
         'alpha':0.7
         }

plt.hist(data1, bins=100, histtype='step', density=True)
plt.text(1.0,0.1,'weight',fontdict=font1,rotation=-60)
plt.show()


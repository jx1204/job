import numpy as np
import matplotlib.pyplot as plt
x = [508,1021,1321,111,1098,1196,204,939,1107,399,474,719,803,1054,1781,525,1050,1362,530,641,903,432,583,894,754,806,1241,1056,1092,1545]#重量
y = [408,921,1329,11,998,1009,104,839,943,299,374,673,703,954,1657,425,950,1375,430,541,971,332,483,815,654,706,1360,956,992,1948]#价值
plt.scatter(x, y)#绘制散点图
plt.xlabel('weight')#横轴
plt.ylabel('profit')#纵轴
plt.title('weight versus profit')#标题
plt.yticks([0,200,400,600,800,1000,1200,1400,1600,1800,2000])
plt.show()

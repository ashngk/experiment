import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = {
    '时间': [10, 20, 30, 40,50,60,70,80,90,100],
    '收入_Jay': [10, 15, 20, 30,20,30,15,30,40,70],
    '收入_JJ': [15, 20, 30, 15,20,20,25,40,30,60],
    '收入_Jolin': [20, 10, 15, 30,10,10,35,40,40,40]
}

plt.figure(figsize=(10, 5))  # 设置画布的尺寸
plt.title('Examples of line chart', fontsize=20)  # 标题，并设定字号大小
plt.xlabel(u'x-year', fontsize=14)  # 设置x轴，并设定字号大小
plt.ylabel(u'y-income', fontsize=14)  # 设置y轴，并设定字号大小

# color：颜色，linewidth：线宽，linestyle：线条类型，label：图例，marker：数据点的类型
plt.plot(data['时间'], data['收入_Jay'], color="deeppink", linewidth=2, linestyle=':', label='Jay income', marker='o')
plt.plot(data['时间'], data['收入_JJ'], color="darkblue", linewidth=1, linestyle='--', label='JJ income', marker='+')
plt.plot(data['时间'], data['收入_Jolin'], color="goldenrod", linewidth=1.5, linestyle='-', label='Jolon income',
         marker='*')

plt.legend(loc=2)  # 图例展示位置，数字代表第几象限
plt.savefig('test5.png', dpi=600)
plt.show()

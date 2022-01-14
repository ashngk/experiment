import matplotlib.pyplot as plt
import numpy as np

a=[37,46]
b=[11,14]
c=[8,16]
index = ['without incentive','with incentive']
# with plt.style.context(['science', 'ieee']):
    # name_list = ['A', 'B', 'C', 'D']
    # num_list = [10, 15, 16, 28]
    # num_list2 = [10, 12, 18, 26]
x = list(range(len(a)))
total_width, n = 0.8, 3
width = total_width / n
plt.bar(x, a, width=width, label='1',  color="red",zorder=10)
for i in range(len(x)):
    x[i] += width
plt.bar(x, b, width=width, label='2', color="black",zorder=10)
for i in range(len(x)):
    x[i] += width
plt.bar(x, c, width=width, label='3', color="blue", zorder=10)
plt.ylabel("Number of participants")
plt.legend(( "students","teachers","graduates"), loc='upper right',fontsize=4)
my_y_ticks = np.arange( 0, 60, 10)
plt.yticks(my_y_ticks)
plt.grid(ls='--', color='black',zorder=0)
plt.savefig('test5.png', dpi = 600)
plt.show()

    # plt.figure()
    # plt.xlabel("Numbers of comments")
    # plt.ylabel("Ratio of accuracy")
    # plt.plot(a,'-',color='blue', linewidth=0.5)
    # plt.plot(b,linewidth=0.5)
    # plt.legend(("Reputation Mechanism", "NO Reputation Mechanism"), loc='upper left',fontsize=4)
    # #
    # my_y_ticks = np.arange( 0, 1, 0.2)
    # plt.yticks(my_y_ticks)
    #
    # plt.savefig('test1.png', dpi = 600)
    # plt.show()


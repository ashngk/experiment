import matplotlib.pyplot as plt
import numpy as np
name_list = ['without incentive','with incentive']
a=[37,46]
b=[11,14]
c=[8,16]
x = list(range(len(a)))
total_width, n = 0.6, 3
width = total_width / n


figsize = 8,6
figure, ax = plt.subplots(figsize=figsize)


# set font for labels in two axis
font1 = {'family': 'Nimbus Roman',
     'weight': 'bold',
     'style':'normal',
     'size': 15,
     }

font2 = {'family': 'Nimbus Roman',
     'weight': 'normal',
     'style':'italic',
     'size': 15,
     }

ax.set_xlabel('without incentive                                          with incentive', font1)
ax.set_ylabel("Number of participants", font1)
ax.set_xticks([])

plt.bar(x, a, width=width, label='students', fc=(58/255, 51/255, 177/255),zorder=10)
for i in range(len(x)):
    x[i] = x[i] + width + 0.01
# plt.bar(x, b, width=width, label='teachers', tick_label=name_list,fc=(178/255, 51/255, 77/255),zorder=10)
plt.bar(x, b, width=width, label='teachers',fc=(178/255, 51/255, 77/255),zorder=10)

for i in range(len(x)):
    x[i] = x[i] + width+0.01
plt.bar(x, c, width=width, label='graduates', fc='0.4',zorder=10)
# plt.ylabel("Number of participants",fontsize=12)
my_y_ticks = np.arange( 0, 60, 10)
plt.yticks(my_y_ticks)
plt.grid(ls='--', color='black',zorder=0)
# plt.xticks(fontsize=12)
plt.legend()
plt.savefig('test_ye.png', dpi = 100)
plt.show()

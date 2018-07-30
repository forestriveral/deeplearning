
import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(-1, 1, 50)
x = np.linspace(-3, 3, 50)
# y = 2*x + 1
y1 = 2*x + 1
# y2 = x**2

plt.figure(num=1, figsize=(8, 5))
# plt.plot(x, y1)

# plt.figure(num=3, figsize=(8, 5))
# plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# plt.xlim((-1, 2))
# plt.ylim((-2, 3))
# plt.xlabel('I am x')
# plt.ylabel('I am y')

# new_ticks = np.linspace(-1, 2, 5)
# print(new_ticks)
# plt.xticks(new_ticks)
# plt.yticks([-2, -1.8, -1, 1.22, 3],
#            ['$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good4', r'$really\ good$'])

# get current axis
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))  # outward, axes
ax.spines['left'].set_position(('data', 0))

# l1, = plt.plot(x, y2, label='up')
# l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
# plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best')

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data',
             xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
plt.text(-3, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16, 'color':'r'})

plt.show()





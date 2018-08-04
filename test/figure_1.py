

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.axis([0, 6, 0, 20])
# plt.show()

# # evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# beijing_x = [h for h in range(0, 24)]
# print(beijing_x)

# x_ = [x_ for x_ in range(0, 24)]
# x_desc = ["{}h".format(x_desc) for x_desc in x_]
# # print(x_desc)
# plt.xticks(x_, x_desc)
# y_ = [y_ for y_ in range(0, 30)][::2]
# # print(y_)
# y_desc = ["{}℃".format(y_desc) for y_desc in y_]
# plt.yticks(y_, y_desc)
# plt.xlabel("Times")
# plt.ylabel("Temperature")
# plt.title("Temperature change in a day")
# plt.legend(loc="best")
# # plt.show()

# y_ = range(0, 50)[::5]
# print(y_)

# time = [131,  98, 125, 131, 124, 139, 131, 117, 128, 108,
#         135, 138, 131, 102, 107, 114, 119, 128, 121, 142,
#         127, 130, 124, 101, 110, 116, 117, 110, 128, 128,
#         115,  99, 136, 126, 134,  95, 138, 117, 111,78,
#         132, 124, 113, 150, 110, 117,  86,  95, 144,
#         105, 126, 130,126, 130, 126, 116, 123, 106,
#         112, 138, 123,  86, 101,  99, 136,123, 117,
#         119, 105, 137, 123, 128, 125, 104, 109, 134,
#         125, 127,105, 120, 107, 129, 116, 108, 132,
#         103, 136, 118, 102, 120, 114,105, 115, 132,
#         145, 119, 121, 112, 139, 125, 138, 109, 132,
#         134,156, 106, 117, 127, 144, 139, 139, 119,
#         140,  83, 110, 102,123,107, 143, 115, 136,
#         118, 139, 123, 112, 118, 125, 109, 119, 133,112,
#         114, 122, 109, 106, 123, 116, 131, 127, 115, 118,
#         112, 135,115, 146, 137, 116, 103, 144,  83, 123,
#         111, 110, 111, 100, 154,136, 100, 118, 119, 133,
#         134, 106, 129, 126, 110, 111, 109, 141,120, 117,
#         106, 149, 122, 122, 110, 118, 127, 121, 114, 125,
#         126,114, 140, 103, 130, 141, 117, 106, 114, 121,
#         114, 133, 137,  92,121, 112, 146,  97, 137, 105,
#         98, 117, 112,  81,  97, 139, 113,134, 106, 144,
#         110, 137, 137, 111, 104, 117, 100, 111, 101, 110,
#         105, 129, 137, 112, 120, 113, 133, 112,  83,  94,
#         146, 133, 101,131, 116, 111,  84, 137, 115, 122,
#         106, 144, 109, 123, 116, 111,111, 133, 150]
# max_time = max(time)
# min_time = min(time)
# width = 5
# num_bins = int((max_time - min_time)/2)
# print(num_bins)
# plt.figure(figsize=(15, 8), dpi=128)
# plt.hist(time, num_bins, color="#509839",density=1)
# x_ = [i for i in range(min_time, max_time+1)]
# plt.xticks(x_[::width])
# plt.grid(True, linestyle="--", alpha=0.5)
# plt.title("Movie runtime")
# plt.savefig("./IMDB.png")
# plt.show()

# evenly sampled time at 200ms intervals
# t = np.arange(0., 5., 0.2)
# print(t)
# red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()
# ===================================================
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# print(data['a'])
# print(data['b'])
# data['d'] = np.abs(data['d']) * 100
# print("========================")
# print(data['d'])
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

# ====================================================

# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
#
# plt.figure(1, figsize=(9, 3))
#
# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()

# x = np.arange(12)
# print(x)
# x = np.linspace(-3, 3, 256)
# print(x)

# x = np.linspace(-3, 3, 50)
# y = 0.1*x
# plt.figure()
# plt.plot(x, y, linewidth=10, zorder=1)
# plt.ylim(-2, 2)
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['bottom'].set_position(('data', 0))
# ax.spines['left'].set_position(('data', 0))
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')
#
# # print(ax.get_xticklabels())
# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     # print(label)
#     label.set_fontsize(12)
#     label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7, zorder=2))
# plt.show()

# T = np.arctan2(Y,X) # for color value

# n = 12
# X = np.arange(n)
# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
# plt.xlim(-.5, n)
# plt.xticks(())
# plt.ylim(-1.25, 1.25)
# plt.yticks(())
#
# for x, y in zip(X, Y1):
#     # print(x)
#     # print(y)
#     # ha: horizontal alignment
#     # va: vertical alignment
#     plt.text(x, y + 0.15, '%.2f' % y, ha='center', va='top',
#              bbox=dict(facecolor='red', alpha=0.5))
#
# for x, y in zip(X, Y2):
#     # ha: horizontal alignment
#     # va: vertical alignment
#     plt.text(x, -y - 0.05, '%.2f' % y, ha='center', va='top')
#
# plt.show()



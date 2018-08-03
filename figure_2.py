
import numpy as np
from numpy import ma
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec

# def f(x, y):
#     # the height function
#     return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 - y**2)
#
#
# n = 256
# x = np.linspace(-3, 3, n)
# y = np.linspace(-3, 3, n)
# X, Y = np.meshgrid(x, y)
# # use plt.contourf to filling contours
# # X, Y and value for (X,Y) point
# plt.contourf(X, Y, f(X, Y), 12, alpha=.75, cmap=plt.cm.hot)
# # use plt.contour to add contour lines
# C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
# # print(C)
# plt.clabel(C, inline=True, fontsize=10)
# plt.xticks(())
# plt.yticks(())
#
# plt.show()


# fig = plt.figure()
# # print(fig)
# ax = Axes3D(fig)
#
# # X, Y value
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
# R = np.sqrt(X ** 2 + Y ** 2)
# # height value
# Z = np.sin(R)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# ax.contourf(X, Y, Z, zdir='z', offset=-1.2, cmap=plt.get_cmap('rainbow'))
#
# plt.show()

plt.figure()

# plt.subplot(2, 2, 1)
# plt.plot([0, 1], [0, 1])
# plt.subplot(2, 2, 2)
# plt.plot([0, 1], [0, 2])
# plt.subplot(223)
# plt.plot([0, 1], [0, 3])
# plt.subplot(224)
# plt.plot([0, 1], [0, 4])

# plt.subplot(2, 1, 1)
# plt.plot([0, 1], [0, 1])
# plt.subplot(2, 3, 4)
# plt.plot([0, 1], [0, 2])
# plt.subplot(235)
# plt.plot([0, 1], [0, 3])
# plt.subplot(236)
# plt.plot([0, 1], [0, 4])

# x = np.arange(0, 10, 0.1)
# y1 = 0.05 * x**2
# y2 = -1 * y1
#
# fig, ax1 = plt.subplots()
# # print(fig)
# # print(ax1)
# ax2 = ax1.twinx()
# ax1.plot(x, y1, 'g-')   # green, solid line
# ax1.set_xlabel('X data')
# ax1.set_ylabel('Y1 data', color='g')
# ax2.plot(x, y2, 'b--')  # blue
# ax2.set_ylabel('Y2 data', color='b', )
#
# plt.show()  # 展示

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# plt.figure(1)
#
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#
# plt.show()

# dt = 0.001
# t = np.arange(0.0, 10.0, dt)
# r = np.exp(-t[:1000]/0.05) # impulse response
# x = np.random.randn(len(t))
# s = np.convolve(x, r)[:len(x)]*dt # colored noise
# # default axes = subplot(111)
# plt.plot(t, s)
# plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
# plt.xlabel('time (s)')
# plt.ylabel('current (nA)')
# plt.title('Gaussian colored noise')
#
# a = plt.axes([.65, .6, .2, .2], facecolor='y')
# n, bins, patches = plt.hist(s, 400, density=1)
# plt.title('Probability')
# # plt.xticks([])
# # plt.yticks([])
#
# # a = plt.axes([0.2, 0.6, .2, .2], facecolor='y')
# # plt.plot(t[:len(r)], r)
# # plt.title('Impulse response')
# # plt.xlim(0, 0.2)
# # plt.xticks([])
# # plt.yticks([])
#
# plt.show()

# ax = plt.subplot2grid((2,2),(0, 0))
# # ax = plt.subplot(2,2,1)
#
# ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
# ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
# ax3 = plt.subplot2grid((3,3), (1, 2), rowspan=2)
# # ax4 = plt.subplot2grid((3,3), (2, 0))
# # ax5 = plt.subplot2grid((3,3), (2, 1))

# plt.show()

# gs = gridspec.GridSpec(2, 2)
# ax = plt.subplot(gs[0, 0])
# gs = gridspec.GridSpec(3, 3)
# ax1 = plt.subplot(gs[0, :])
# ax2 = plt.subplot(gs[1,:-1])
# ax3 = plt.subplot(gs[1:, -1])
# ax4 = plt.subplot(gs[-1,0])
# ax5 = plt.subplot(gs[-1,-2])

# plt.show()

# gs1 = gridspec.GridSpec(3, 3)
# gs1.update(left=0.05, right=0.48, wspace=0.05)
# ax1 = plt.subplot(gs1[:-1, :])
# ax2 = plt.subplot(gs1[-1, :-1])
# ax3 = plt.subplot(gs1[-1, -1])
# gs2 = gridspec.GridSpec(3, 3)
# gs2.update(left=0.55, right=0.98, hspace=0.05)
# ax4 = plt.subplot(gs2[:, :-1])
# ax5 = plt.subplot(gs2[:-1, -1])
# ax6 = plt.subplot(gs2[-1, -1])
#
# plt.show()

# x = np.arange(0, 2*np.pi, 0.02)
# y = np.sin(x)
# y1 = np.sin(2*x)
# y2 = np.sin(3*x)
# ym1 = np.ma.masked_where(y1 > 0.5, y1)
# ym2 = np.ma.masked_where(y2 < -0.5, y2)
#
# lines = plt.plot(x, y, x, ym1, x, ym2, 'o')
# plt.setp(lines[0], linewidth=4)
# plt.setp(lines[1], linewidth=2)
# plt.setp(lines[2], markersize=10)
# #
# plt.legend(('No mask', 'Masked if > 0.5', 'Masked if < -0.5'),
#            loc='upper right')
# plt.title('Masked line demo')
# plt.show()

x = np.arange(1, 7, 0.4)
y0 = np.sin(x)
y = y0.copy() + 2.5

plt.step(x, y, label='pre (default)')
y -= 0.5
plt.step(x, y, where='mid', label='mid')
y -= 0.5
plt.step(x, y, where='post', label='post')
y = ma.masked_where((y0 > -0.15) & (y0 < 0.15), y - 0.5)
plt.step(x, y, label='masked (pre)')
#
# plt.legend()
# plt.xlim(0, 7)
# plt.ylim(-0.5, 4)

plt.show()



from matplotlib.ticker import NullFormatter  # useful for `logit` scale
import matplotlib
import numpy as np
from numpy import ma
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches

# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
#
# # the histogram of the data
# n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)
#
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# left, width = .25, .5
# bottom, height = .25, .5
# right = left + width
# top = bottom + height
#
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
# p = patches.Rectangle(
#     (left, bottom), width, height,
#     fill=False, transform=ax.transAxes, clip_on=False)
# ax.add_patch(p)

# ax.text(left, bottom, 'left top',
#         horizontalalignment='left',
#         verticalalignment='top',
#         transform=ax.transAxes)
#
# ax.text(left, bottom, 'left bottom',
#         horizontalalignment='left',
#         verticalalignment='bottom',
#         transform=ax.transAxes)
# #
# ax.text(right, top, 'right bottom',
#         horizontalalignment='right',
#         verticalalignment='bottom',
#         transform=ax.transAxes)
# #
# ax.text(right, top, 'right top',
#         horizontalalignment='right',
#         verticalalignment='top',
#         transform=ax.transAxes)
# #
# ax.text(right, bottom, 'center top',
#         horizontalalignment='center',
#         verticalalignment='top',
#         transform=ax.transAxes)
# #
# ax.text(left, 0.5*(bottom+top), 'right center',
#         horizontalalignment='right',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
# #
# ax.text(left, 0.5*(bottom+top), 'left center',
#         horizontalalignment='left',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
#
# ax.text(0.5*(left+right), 0.5*(bottom+top), r'$\sum_{i=0}^\infty x_i$',
#         horizontalalignment='center',
#         verticalalignment='center',
#         fontsize=20, color='red',
#         transform=ax.transAxes)
#
# ax.text(right, 0.5*(bottom+top), 'centered',
#         horizontalalignment='center',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
# #
# ax.text(left, top, 'rotated\nwith newlines',
#         horizontalalignment='center',
#         verticalalignment='center',
#         rotation=45,
#         transform=ax.transAxes)
#
# ax.set_axis_off()
# plt.show()

# np.random.seed(19680801)
# # example data
# mu = 100  # mean of distribution
# sigma = 15  # standard deviation of distribution
# x = mu + sigma * np.random.randn(437)
# print(x)
# num_bins = 100
# fig, ax = plt.subplots()
# # the histogram of the data
# n, bins, patches = ax.hist(x, num_bins, density=4)
# print(n, "=====", bins, "=====", patches)
# # add a 'best fit' line
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
#      np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
# ax.plot(bins, y, '--')
# ax.set_xlabel('Smarts')
# ax.set_ylabel('Probability density')
# ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
# # Tweak spacing to prevent clipping of ylabel
# fig.tight_layout()
# plt.show()


# Fixing random state for reproducibility
np.random.seed(19680801)
# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))
# plot with various axes scales
plt.figure(1)
# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)
# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)
# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)
# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=1.25,
                    wspace=0.35)

plt.show()


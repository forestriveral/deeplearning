
import matplotlib.pyplot as plt
from random import choice

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)
#
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', labelsize=14)
#
# plt.show()

# # x_value = [1, 2, 3, 4, 5]
# x_values = list(range(1, 1001))
# # y_value = [1, 4, 9, 16, 25]
# y_values = [x**2 for x in x_values]
# plt.scatter(x_values, y_values, s=10, c=y_values, edgecolors='none',
#             cmap=plt.cm.Blues)
#
# plt.title("Square Numbers", fontsize=24, )
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.axis([0, 1100, 0, 1100000])
#
# # plt.show()
# plt.savefig('square_plot.png', bbox_inches='tight')


class Randomwalker(object):

    def __init__(self, num_points=50000):
        """Initialize the random walker"""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """Determine the walk direction and calculate the walk steps"""
        step_direction = choice([1, -1])
        step_distance = choice([0, 1, 2, 3, 4])
        step = step_direction * step_distance
        return step

while True:
    rw = Randomwalker()
    rw.fill_walk()
    # set the size of plot window
    plt.figure(dpi=128, figsize=(10, 6))
    # show color map
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1, zorder=1)
    # starts and ends
    plt.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=100, zorder=2)
    # hide the axix
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # show plot
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

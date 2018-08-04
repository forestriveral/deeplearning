
import pygal as pg
from random import randint


class Die():
    """Represent a die."""
    def __init__(self, num_side=6):
        self.num_sides = num_side

    def roll(self):
        """Return a random value between 1 and num_side"""
        return randint(1, self.num_sides)

# two dice
die_1 = Die()
die_2 = Die()

# Roll die
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analysis results
# frequencies = []
max_results = die_1.num_sides + die_2.num_sides
# for value in range(2, max_results + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2, max_results+1)]

# data visualization
hist = pg.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_labels = [str(x) for x in range(2, max_results+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('two_die_visual.svg')

# print(frequencies)

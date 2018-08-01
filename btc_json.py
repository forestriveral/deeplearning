

# from __future__ import (absolute_import, division,
#                         print_function, unicode_literals)
# from urllib.request import urlopen
import json
import pygal
import math

filename = 'dataset/btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = int(btc_dict['month'])
#     week = int(btc_dict['week'])
#     weekday = btc_dict['weekday']
#     close = int(float(btc_dict['close']))
#     print("{} is month {} week {}, {}, the close price is {} RMB".format(
#         date, month, week, weekday, close))

dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_label=False)
line_chart.title = 'Log closing price($)'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
# log
close_log = [math.log10(_) for _ in close]
line_chart.add("Log closing price", close_log)
line_chart.render_to_file("dataset/log_closing_price_line_diagram.svg")
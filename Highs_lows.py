
import csv
from matplotlib import pyplot as plt
from datetime import datetime
'''
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # date
    dates, highs, lows = [], [], []
    # highs = []
    for row in reader:
        # when data loss
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # print(highs)

fig = plt.figure(dpi=128, figsize=(10, 6))
# high temperature
plt.plot(dates, highs, c='red', alpha=0.5)
# low temperature
plt.plot(dates, lows, c='blue', alpha=0.5)
# color fill
plt.fill_between(dates, highs, lows, facecolors='blue', alpha=0.1)

# format
plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA",
          fontsize=24)
plt.xlabel("", fontsize=16)
# date formatted
fig.autofmt_xdate()
plt.ylabel("Temperture(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
# axis limitation
plt.ylim(10, 120)
plt.show()
'''
print("========================================")

def get_weather_data(filename, data, highs, lows):
    """Get the highs and lows from a data files."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # date
        # dates, highs, lows = [], [], []
        # highs = []
        for row in reader:
            # when data loss
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except:
                print(current_date, "missing data")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Get weather data for Sitka
dates, highs, lows = [], [], []
get_weather_data("sitka_weather_2014.csv", dates, highs, lows)
# Plot Sitka weather data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)
# Get Death Valley data.
dates, highs, lows = [], [], []
get_weather_data('death_valley_2014.csv', dates, highs, lows)
# Add Death Valley data to current plot.
plt.plot(dates, highs, c='red', alpha=0.3)
plt.plot(dates, lows, c='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)
# Format plot.
title = "Daily high and low temperatures - 2014"
title += "\nSitka, AK and Death Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 120)

plt.show()

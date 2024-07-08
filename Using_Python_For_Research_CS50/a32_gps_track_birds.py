import pandas as pd

birddata = pd.read_csv("bird_tracking.csv")

# birddata.info()
# birddata.head()

# Plot latitude and longitude on a 2D plot
import matplotlib.pyplot as plt
import numpy as np
# plt.figure(figsize=(7,7))

#indexes_of_eric = birddata.bird_name == "Eric"
#x, y = birddata.longitude[indexes_of_eric], birddata.latitude[indexes_of_eric]
#print("Longitude + latitude", x, y)
# plt.plot(x,y, ".") # Dots as plot points for Eric
# plt.show()

# All birds (3)
bird_names = pd.unique(birddata.bird_name)
#print(bird_names)

# for bird_name in bird_names:
#     ix = birddata.bird_name == bird_name # ix -  Indexes of birds
#     x, y = birddata.longitude[ix], birddata.latitude[ix]
#     plt.plot(x,y, ".", label=bird_name) # Dots as plot points for index names
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.legend(loc="lower right")
#plt.savefig("3_bird_trajectories.pdf")
#plt.show()


# examine 2D flight speed of the birds

#ix = birddata.bird_name == "Eric"
#speed = birddata.speed_2d[ix]
#plt.hist(speed[:10])
#plt.show()

# Check if any value is NaN - Not a Number
#print(np.isnan(speed).any())
#print(np.sum(np.isnan(speed).any())) # Sum of NaN

#ind = np.isnan(speed) # Only numbers
#print(~ind) # Switch, reverse, False to True


# ix = birddata.bird_name == "Eric"
# speed = birddata.speed_2d[ix]
# ind = np.isnan(speed)
# plt.hist(speed[~ind])
# plt.show()



# plt.figure(figsize=(8,4))
# speed = birddata.speed_2d[birddata.bird_name == "Eric"]
# ind = np.isnan(speed)
# plt.hist(speed[~ind], bins=np.linspace(0, 30, 20))
# plt.xlabel("2D speed (m/s) with pyplot")
# plt.ylabel("Frequency")
# plt.show()



# Histogram in Pandas
# birddata.speed_2d.plot(kind = "hist", range=[0, 30])
# plt.xlabel("2D speed with Pandas")
# plt.show()



# measure elapsed time, timestamped events
# print(birddata.date_time[0:5]) # 0    2013-08-15 00:18:08+00

import datetime
# # Convert timestamps to datetime objects
# time_1 = datetime.datetime.today()
# print(time_1)
# time_2 = datetime.datetime.today()
# print(time_2 - time_1) # Timedelta object

# date_str = birddata.date_time[0]
# print(date_str)
# print(date_str[:-3])

# print(datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S"))

timestamps = []
for k in range(len(birddata)):
    timestamps.append(datetime.datetime.strptime\
    (birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S"))
# print(timestamps[:5])
# print(timestamps[0])

# # Create Panda series object and insert timestamps
birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
# print(birddata.head())
# print(birddata.timestamp[5] - birddata.timestamp[0])


# times = birddata.timestamp[birddata.bird_name == "Eric"]
# elapsed_time = [time - times[0] for time in times]
# print(elapsed_time[1000])

# print(elapsed_time[1000] / datetime.timedelta(days = 1)) # How much days passed from first timestamp
# print(elapsed_time[1000] / datetime.timedelta(hours = 1)) # Hours


# # Make plot for timestamps
# plt.plot(np.array(elapsed_time) / datetime.timedelta(days = 1))
# plt.xlabel("Observation")
# plt.ylabel("Elapsed time (days)")
# plt.savefig("timeplot.pdf")
# plt.show()


# Calculate daily mean speed
# Calculate mean speed per day

data = birddata[birddata.bird_name == "Eric"]
times = data.timestamp
elapsed_time = [time - times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days = 1)

next_day = 1
inds = []
daily_mean_speed = []
for (i, t) in enumerate(elapsed_days): # i-index, t-time
    if t < next_day:
        inds.append(i)
    else: 
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []

plt.figure(figsize = (8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed m/s")
plt.savefig("mean_daily_speed.pdf")
plt.show()


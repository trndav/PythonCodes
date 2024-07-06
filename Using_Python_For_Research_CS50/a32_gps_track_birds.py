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



plt.figure(figsize=(8,4))
speed = birddata.speed_2d[birddata.bird_name == "Eric"]
ind = np.isnan(speed)
plt.hist(speed[~ind], bins=np.linspace(0, 30, 20))
plt.xlabel("2D speed (m/s) with pyplot")
plt.ylabel("Frequency")
plt.show()



# Histogram in Pandas
birddata.speed_2d.plot(kind = "hist", range=[0, 30])
plt.xlabel("2D speed with Pandas")
plt.show()
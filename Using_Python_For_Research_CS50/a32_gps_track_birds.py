import pandas as pd

birddata = pd.read_csv("bird_tracking.csv")

# birddata.info()
# birddata.head()

# Plot latitude and longitude on a 2D plot
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(7,7))

#indexes_of_eric = birddata.bird_name == "Eric"
#x, y = birddata.longitude[indexes_of_eric], birddata.latitude[indexes_of_eric]
#print("Longitude + latitude", x, y)
# plt.plot(x,y, ".") # Dots as plot points for Eric
# plt.show()

# All birds (3)
bird_names = pd.unique(birddata.bird_name)
print(bird_names)

for bird_name in bird_names:
    ix = birddata.bird_name == bird_name # ix -  Indexes of birds
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y, ".", label=bird_name) # Dots as plot points for index names
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower right")
plt.savefig("3_bird_trajectories.pdf")
plt.show()


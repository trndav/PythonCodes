# Pandas serie - 1d, dataframe +2d
import pandas as pd
import numpy as np

# x2 = pd.Series([6,3,8,6])
# print(x2)

# x3 = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])
# print(f"{x3} \n {x3[['w', 'r', 'q']]}")

# age = {"Tim": 29, "Jim": 31, "Pam": 27, "Sam": 35}
# x4 = pd.Series(age) # Keys are sorted
# print(x4)


# data = {"name": ["Tim", "Jim", "Pam", "Sam"],
#         "age": [29, 31, 27, 35],
#         "ZIP": ["10000", "12100", "10200", "45111"]}
# x = pd.DataFrame(data, columns = ["name", "age", "ZIP"])
# print(x)
# print(x["name"])
# print(x.name)


# y = pd.Series([6,3,8,6], index = ["q", "w", "e", "r"])
# print(y.index)
# print(sorted(y.index))
# c = y.reindex(sorted(y.index)) # Reindex - sort indexes in different order
# print(c)


# a = pd.Series([2,3,1,4], index = ["e", "q", "r", "t"])
# print(a + y) # Sum by indexes, e + e = 8 + 2



whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt") # Add new column to whisky variable
print(whisky.head())

# print(whisky.iloc[0:10])
# print(whisky.iloc[6:11, 0:5]) # Show specific rows and columns

# print(whisky.columns) # List names of columns
flavors = whisky.iloc[:, 2:14] # Row columns
# print(flavors)

# Explore correlation - Pearson correlation
corr_flavors = pd.DataFrame.corr(flavors) # - correlation
# print(corr_flavors)

import matplotlib.pyplot as plt
# plt.figure(figsize=(10,10))
# plt.pcolor(corr_flavors) # -pcolor plot a correlation matrix by color
# plt.colorbar()
# plt.savefig("corr_flavors.pdf")

corr_whisky = pd.DataFrame.corr(flavors.transpose()) # Transpose, revert x for y
# plt.figure(figsize=(10,10))
# plt.pcolor(corr_whisky)
# plt.colorbar()
# plt.savefig("corr_whisky.pdf")
# plt.show()


# Spectral co-clustering, eigenvalues, eigenvectors
from sklearn.cluster import SpectralCoclustering

model = SpectralCoclustering(n_clusters = 6, random_state = 0)
model.fit(corr_whisky)
''' .rows_ is a convention used in scikit-learn to differentiate between the parameters that are passed 
when creating the model and attributes that are calculated or set when the model is fitted.'''
#print(model.rows_)

print(np.sum(model.rows_, axis = 1)) # How many whiskey belong to cluster 1, 2, 3..
print(np.sum(model.rows_, axis = 0))
print(model.row_labels_)


whisky["Group"] = pd.Series(model.row_labels_, index = whisky.index) # Order by group labels (spectral cocluster)
whisky = whisky.iloc[np.argsort(model.row_labels_)] # Reset index of dataframe
whisky = whisky.reset_index(drop=True) # Reshuffled columns and rows

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose()) # Correlation on all rows 2:14 columns
correlations = np.array(correlations)

plt.figure(figsize = (14, 4))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlations.pdf")
# Whiskey in same blocks (squares) are more similar in taste, flavor
plt.show()

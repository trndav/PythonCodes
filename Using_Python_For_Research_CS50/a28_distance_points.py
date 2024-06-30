import numpy as np
import random
import matplotlib.pyplot as plt

# p1 = np.array([1, 1])
# p2 = np.array([4, 4])

# # Calculate distance between 2 points
# # print(p2 - p1)
# # print(np.power(p2 - p1, 2))
# # print(np.sum(np.power(p2 - p1, 2)))
# # print(np.sqrt(np.sum(np.power(p2 - p1, 2))))


# # Function calculate distance 2 points
def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))
# # print(distance(p1, p2))


# # Calculate most occurances (votes)
def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    return vote_counts
# # votes = [1,2,3,1,2,2,2,3,3,3,3,3,3]
# # vote_counts = majority_vote(votes)
# # print("vote_counts", vote_counts)
# # print("max vote_counts", max(vote_counts))
# # print("max vote_counts.keys", max(vote_counts.keys()))
# # print("max vote_counts.values", max(vote_counts.values()))

# # max_count = max(vote_counts.values())


# # # Calculate winner - most votes/occurances
# # winners = []
# # for vote, count in vote_counts.items():
# #     #print("Vote, count", vote, count)
# #     if count == max_count:
# #         winners.append(vote)
# # print("Winners", winners)


# votes = [1,2,3,1,2,2,2,3,3,3,3,3,3,2,2,2]
# # Calculate most occurances (votes)
def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winners = []
    max_count = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
    return random.choice(winners) # Return 1 winner even if it is a tie
#winner = majority_vote(votes)
# # print(winner)


# # Return most comon element using scipy.stats
# import scipy.stats as ss
# votes = [1,2,3,1,2,2,2,3,3,3,3,3,3,2,2,2]

# def majority_vote_short(votes):
#     mode, count = ss.mstats.mode(votes)
#     return mode, count
# winner = majority_vote_short(votes)
# # print(winner)



# # Finding kNN - nearest neighbors
points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]]) # Numpy expects 1 list
p = np.array([1.3, 1.2])
p2 = np.array([[1.3, 1.2, 5], [4, 6, 5]])
# #print(p2.shape)

def find_nearest_neighbors(p, points, k=5):
    '''Find k nearest neighbor of point p'''
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]
# # print(f"Closest point indexes are:", find_nearest_neighbors(p, points, 4))
# ind = find_nearest_neighbors(p, points, 4)
# #print(f"Closest point indexes are:", find_nearest_neighbors(p, points, 4))
# #print(f"Points closest to {p} are:", points[ind])

distances = np.zeros(points.shape[0])
for i in range(len(distances)):
    distances[i] = distance(p, points[i])
# # print(distances)
# # print(distances[4])
# # Sort array by indices
# ind = np.argsort(distances)
# # print(ind) # index 4 and 7 of distances, is closest to p


# #plt.plot(points[:,0], points[:,1], "ro")
# #plt.plot(p[0], p[1], "bo")
# #plt.show()



def knn_predict(p, points, outcomes, k=5): # outcomes, to predict classes
    '''Predict class of p based on majority vote'''
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])

# outcomes = np.array([0,0,0,0,1,1,1,1,1]) # 9 points, 9 outcomes - 9 classes
# #print(knn_predict(p, points, outcomes, k=3))
# #print(knn_predict([2.2, 2.5], points, outcomes, k=5))



# # Generate synthetic data
import scipy.stats as ss
# #print(ss.norm(0,1).rvs((5,2))) # mean standard deviation 0-1
# #print(ss.norm(1,1).rvs((5,2)))
# ss.norm(0,1).rvs((5,2))
# ss.norm(1,1).rvs((5,2))
print("*"*20)
# # Concatenate array:
# #print(np.concatenate((ss.norm(0,1).rvs((5,2)), ss.norm(1,1).rvs((5,2))), axis=0))

# n = 50
# np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
# #print(np.concatenate((np.repeat(0, n), np.repeat(0, n))))
# outcomes = np.concatenate((np.repeat(0, n), np.repeat(0, n)))


def generate_synth_data(n=50):
    '''Create 2 sets of points from bivariate normal distributions.'''
    points = np.concatenate((ss.norm(0,1).rvs((n,2)), ss.norm(1,1).rvs((n,2))), axis=0)
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(0, n)))
    return (points, outcomes)
#print(generate_synth_data(3))
(points, outcomes) = generate_synth_data(15)
#print(points, outcomes)

# print(points[n:,0])
# plt.figure()
# plt.plot(points[:n,0], points[:n,1], "bo")
# plt.plot(points[n:,0], points[n:,1], "ro")
# plt.savefig("knn_synth_50.pdf")
#plt.show()


# Prediction grid
def make_prediction_grid(predictors, outcomes, limits, h, k):
    '''Classify each point on the prediction grid.'''
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h) #h =increment
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype = int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)
    return (xx, yy, prediction_grid)



def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)


(predictors, outcomes) = generate_synth_data()
# print(predictors.shape)
k=5; filename="iris_grid.pdf"; limits = (4,8,-1.5,4.5); h = 0.1
(xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
plot_prediction_grid(xx, yy, prediction_grid, filename)
#plt.show()



# Sklearn
from sklearn import datasets
iris = datasets.load_iris()
#print(iris["data"])

predictors = iris.data[:, 0:2]
outcomes = iris.target
plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], "ro")
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], "go")
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], "bo")
plt.savefig("iris.pdf")
#plt.show()



from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)
print(sk_predictions.shape)

my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])
print(my_predictions.shape)
print(sk_predictions == my_predictions)
print("Percentage of similarity:", 100*np.mean(sk_predictions == my_predictions))

print("Percentage of sk_predictions:", 100*np.mean(sk_predictions == outcomes))
print("Percentage of my_predictions:", 100*np.mean(my_predictions == outcomes))
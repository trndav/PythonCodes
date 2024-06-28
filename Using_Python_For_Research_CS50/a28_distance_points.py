import numpy as np
import random

p1 = np.array([1, 1])
p2 = np.array([4, 4])

# Calculate distance between 2 points
# print(p2 - p1)
# print(np.power(p2 - p1, 2))
# print(np.sum(np.power(p2 - p1, 2)))
# print(np.sqrt(np.sum(np.power(p2 - p1, 2))))


# Function calculate distance 2 points
def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))
# print(distance(p1, p2))


# Calculate most occurances (votes)
# def majority_vote(votes):
#     vote_counts = {}
#     for vote in votes:
#         if vote in vote_counts:
#             vote_counts[vote] += 1
#         else:
#             vote_counts[vote] = 1
#     return vote_counts
# votes = [1,2,3,1,2,2,2,3,3,3,3,3,3]
# vote_counts = majority_vote(votes)
# print("vote_counts", vote_counts)
# print("max vote_counts", max(vote_counts))
# print("max vote_counts.keys", max(vote_counts.keys()))
# print("max vote_counts.values", max(vote_counts.values()))

# max_count = max(vote_counts.values())


# # Calculatze winner - most votes/occurances
# winners = []
# for vote, count in vote_counts.items():
#     #print("Vote, count", vote, count)
#     if count == max_count:
#         winners.append(vote)
# print("Winners", winners)


votes = [1,2,3,1,2,2,2,3,3,3,3,3,3,2,2,2]
# Calculate most occurances (votes)
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
winner = majority_vote(votes)
# print(winner)


# Return most comon element using scipy.stats
import scipy.stats as ss
votes = [1,2,3,1,2,2,2,3,3,3,3,3,3,2,2,2]

def majority_vote_short(votes):
    mode, count = ss.mstats.mode(votes)
    return mode, count
winner = majority_vote_short(votes)
# print(winner)



# Finding kNN - nearest neighbors
points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]]) # Nupy expects 1 list
p = np.array([1.3, 1.2])
p2 = np.array([[1.3, 1.2, 5], [4, 6, 5]])
print(p2.shape)

def find_nearest_neighbors(p, points, k=5):
    '''Find k nearest neighbor of point p'''
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]
# print(f"Closest point indexes are:", find_nearest_neighbors(p, points, 4))
ind = find_nearest_neighbors(p, points, 4)
print(f"Closest point indexes are:", find_nearest_neighbors(p, points, 4))
print(f"Points closest to {p} are:", points[ind])

distances = np.zeros(points.shape[0])
for i in range(len(distances)):
    distances[i] = distance(p, points[i])
# print(distances)
# print(distances[4])
# Sort array by indices
ind = np.argsort(distances)
# print(ind) # index 4 and 7 of distances, is closest to p

import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")
plt.show()



def knn_predict(p, points, outcomes, k=5): # outcomes, to predict classes
    '''Predict class of p based on majority vote'''
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])

outcomes = np.array([0,0,0,0,1,1,1,1,1]) # 9 points, 9 outcomes - 9 classes
#print(knn_predict(p, points, outcomes, k=3))
print(knn_predict([2.2, 2.5], points, outcomes, k=5))
import numpy as np  
import scipy.stats as ss
import matplotlib.pyplot as plt

n = 100 # data points
beta_0 = 5
beta_1 = 2
np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n) # outcome data

# print(np.mean(x))
# print(np.mean(y))

# plt.figure()
# plt.plot(x, y, "o", ms=5)
# xx = np.array([0, 10]) # values to plot regression function
# plt.plot(xx, beta_0 + beta_1 * xx)
# plt.xlabel(("x"))
# plt.ylabel(("y"))
# plt.show()


# Linear regression
def compute_rss(y_estimate, y):
  return sum(np.power(y - y_estimate, 2))
def estimate_y(x, b_0, b_1):
  return b_0 + b_1 * x
rss = compute_rss(estimate_y(x, beta_0, beta_1), y)
#print(rss)

# Least Squares Estimation in Code

rss = []
slopes = np.arange(-10, 15, 0.01)
for slope in slopes:
    rss.append(np.sum(y - beta_0 - slope * x) ** 2)
# print(rss)

ind_min = np.argmin(rss)
# print(ind_min)
#print("Estimate of slope: ", slopes[ind_min])

# plt.figure()
# plt.plot(slopes, rss)
# plt.xlabel(("Slope"))
# plt.ylabel(("RSS"))
# plt.show()


import statsmodels.api as sm
mod = sm.OLS(y, x)
est = mod.fit()
print(est.summary())

X = sm.add_constant(x)
mod = sm.OLS(y, X)
est = mod.fit()
#print(est.summary())


# Multiple Linear Regression
# scikit-learn for Linear Regression

n = 500
beta_0 = 5
beta_1 = 2
beta_2 = -1
np.random.seed(1)
x_1 = 10 * ss.uniform.rvs(size=n)
x_2 = 10 * ss.uniform.rvs(size=n)
y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc = 0, scale = 1, size = n)

X = np.stack([x_1, x_2], axis = 1)

from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:,0], X[:,1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$")
#plt.show()


from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Ako trebate normalizirati podatke, koristite StandardScaler
model = make_pipeline(StandardScaler(), LinearRegression())
model.fit(X, y)

intercept = model.named_steps['linearregression'].intercept_
coef = model.named_steps['linearregression'].coef_

# lm  = LinearRegression(fit_intercept = True)
# lm.fit(X, y)
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print(intercept)
print(coef[0])
print(coef[1])
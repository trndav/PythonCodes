# Linear regression

from sklearn.linear_model import LinearRegression 
import numpy as np

x = np.array([[500], [1000], [1500], [2000], [2500]])
y = np.array([150, 300, 450, 600, 750])

model = LinearRegression()
model.fit(x, y)

c = 1500
new_house_size = np.array([[c]])
predicted_price = model.predict(new_house_size)

print(f"The predicted price for size {c} house is: {predicted_price[0]:.2f}$.")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

dataset = pd.read_csv('C:/Users/c7371613/Downloads/weight-height.csv')

# Checking dataset
print(dataset.head())

# Checking for null values
print(dataset.isnull().sum())

# # Checking dimensions
print('Dimension of the dataset:')
print(dataset.shape)

# Plotting gender vs weight
x1 = dataset.iloc[:,0].values
y1 = dataset.iloc[:,2].values

print(x1)
print(y1)

plt.scatter(x1,y1, label= 'Gender', color='Green', s=50)
plt.xlabel('Gender')
plt.ylabel('Weight')
plt.title('Gender vs Weight')
plt.legend()
plt.show()

# Plotting height vs weight
x2= dataset.iloc[:,1].values
y2 = dataset.iloc[:,2].values
plt.scatter(x2,y2, label= 'Height', color='Orange', s=50)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height vs Weight')
plt.legend(loc='lower right')
plt.show()

# separating independent and dependant variable
# X-Independent variable
X= dataset.iloc[:,1:2].values
print(X)

# X-dependent or target variable
y= dataset.iloc[:,2].values
print(y)

# splitting dataset into training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# creating linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


#checking accuracy
#predicting test set results
y_pred = regressor.predict(X_test)
print('Coefficients:', regressor.coef_)
# mean squared error
print('Mean squared error: %.2f' % np.mean((regressor.predict(X_test)- y_test) ** 2))
# Explained variance score: 1 is a perfect prediction
print('Variance score: %.2f')
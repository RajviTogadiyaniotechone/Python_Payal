import sklearn
print(sklearn.__version__)

from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print(X_scaled)



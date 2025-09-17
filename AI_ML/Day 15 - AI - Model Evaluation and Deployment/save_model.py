import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Example data (you should replace this with your actual dataset)
X_train = np.array([[1, 2], [3, 4], [5, 6]])  # Features
y_train = np.array([0, 1, 0])                 # Labels

# Train the model (example with RandomForestClassifier)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model to a pickle file
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Model saved successfully as 'model.pkl'!")

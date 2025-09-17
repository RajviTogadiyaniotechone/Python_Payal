import streamlit as st
import pickle
import numpy as np

# Step 1: Load the trained model (Make sure the model.pkl file exists)
try:
    with open('model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Step 2: Title for the app
st.title("Machine Learning Model Prediction")

# Step 3: Instructions for the user
st.write("Enter the feature values to get a prediction:")

# Step 4: Collect feature inputs from the user
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)

# Add more features as needed (based on what your model expects)

# Step 5: Create an array with the input values
features = np.array([feature1, feature2]).reshape(1, -1)

# Step 6: Button to trigger prediction
if st.button("Predict"):
    try:
        # Step 7: Make the prediction using the loaded model
        prediction = model.predict(features)
        
        # Step 8: Display the prediction result
        st.write(f"Prediction: {prediction[0]}")
    except Exception as e:
        st.error(f"Error making prediction: {e}")

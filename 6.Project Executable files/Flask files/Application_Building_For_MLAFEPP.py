# Import the necessary libraries
from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the saved model
final_model = joblib.load("C:/Users/akash/OneDrive/Documents/SmartBridge_Extenship/garments_model_Final.pkl")

# Function to predict productivity level
def predict_productivity(data):
    prediction = final_model.predict(data)
    if prediction >= 0.7:
        result = "Highly Productive"
    elif prediction >= 0.5:
        result = "Medium Productive"
    else:
        result = "Low Productive"
    return result

# Initialize the Flask application
app = Flask(__name__)

# Define routes to render HTML pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    return render_template('predict.html')

@app.route('/submit', methods=['POST'])
def pred():
    if request.method == 'POST':
        # Retrieve the values entered by the user
        features = [float(x) for x in request.form.values()]
        # Reshape the data to match the model's input shape
        data = np.array(features).reshape(1, -1)
        # Get productivity prediction using the predictive system
        productivity_level = predict_productivity(data)
        # Render the submit.html page with the predicted productivity level
        return render_template('submit.html', productivity_level=productivity_level)
    
# Define route for about page
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)

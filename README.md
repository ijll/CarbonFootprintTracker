# CarbonFootprintTracker
EcoTrack - Carbon Footprint Tracker
<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# Icon app footprint carbon
![](CarbonFootPrinter.jpeg)

# EcoTrack - Carbon Footprint Tracker

Final project for the Building AI course

## Summary

EcoTrack is an platform designed to help individuals and businesses track, analyze, and reduce their carbon footprint in real-time. By integrating data from daily activities, purchases, and energy usage, EcoTrack provides personalized recommendations to promote sustainable living and operational efficiency.


## Background

Climate change is one of the most pressing challenges of our time, with carbon emissions being a significant contributor. While many people and organizations want to reduce their environmental impact, they often lack the tools to measure and understand their carbon footprint effectively.

·	Problem: There is no easy, automated way for individuals or small businesses to track their carbon emissions comprehensively.
·	Frequency: This is a global issue affecting billions of people and millions of businesses daily.
·	Personal Motivation: As someone passionate about sustainability, I want to empower people to make informed decisions that benefit the planet.
·	Importance: Reducing carbon emissions is critical to mitigating climate change, and awareness is the first step toward action.

## How is it used?

·	Context: EcoTrack would be used by individuals, households, and small businesses to monitor their environmental impact.
·	Users:
  ·	Individuals: Track daily activities like commuting, shopping, and energy use.
  ·	Businesses: Monitor supply chain emissions and office energy consumption.
·	Impact: Users gain insights into their carbon footprint and receive actionable recommendations to reduce it.


## Data sources and AI methods

  1.	User-input data (e.g., transportation habits, energy usage, dietary preferences).
  2.	APIs from services like utility providers, e-commerce platforms, and transportation apps.
  3.	Public datasets on carbon emissions for products, services, and activities.

## Challenges

  1.	Data Accuracy: Reliance on user-input data may lead to inaccuracies.
  2.	Scope Limitations: The tool may not account for all indirect emissions (e.g., embedded carbon in products).
  3.	Adoption: Encouraging users to consistently input data and follow recommendations may be difficult.

## What next?

  1.	Expand Data Sources: Partner with companies to integrate real-time data from smart devices, apps, and IoT sensors.
  2.	Gamification: Add features like challenges, rewards, and social sharing to encourage sustainable behavior.
  3.	Policy Integration: Work with governments to provide carbon credits or incentives based on EcoTrack usage.
  4.	Global Scale: Localize the platform for different regions, accounting for varying carbon emission factors.

## Acknowledgments

·	Open-source libraries like TensorFlow, Scikit-learn, and Hugging Face for AI models.
·	Public datasets from organizations like the EPA and UK Government.
·	Inspiration from existing tools like Oroeco and Carbon Footprint Calculator.

## How to Contribute

I welcome contributions to the EcoTrack project! Here’s how you can get involved:
  1.	Fork the repository and create a new branch for your feature or improvement.
  2.	Submit a pull request with a detailed description of your changes.
  3.	Join the discussion in the Issues section to suggest ideas or report bugs.

## How It Works

  1.	The user selects an activity and inputs the time spent on it (e.g., hours of driving per year).
  2.	The app uses a pre-trained machine learning model to predict the carbon footprint based on the activity.
  3.	The result is displayed on the result.html page.

## Next Steps

  1.	Expand Data: Use a more comprehensive dataset with accurate carbon emission factors.
  2.	Add More Features: Include recommendations for reducing carbon footprints.
  3.	Integrate APIs: Connect to APIs for real-time data (e.g., energy usage, transportation).
  4.	Deploy: Host the app on a cloud platform like Heroku or AWS.

This is a basic prototype to get started. You can expand it further based on your goals and resources!

## Code Implementation

1. Install Required Libraries
First, install the required libraries:
bash

pip install flask scikit-learn pandas numpy

2. Python Code

Import librariesfrom flask import Flask, request, render_template import pandas as pd import numpy as np from sklearn.ensemble import RandomForestRegressor from sklearn.model_selection import train_test_split  # Initialize Flask app app = Flask(__name__)# Load a sample dataset (for demonstration)# In a real-world scenario, use a comprehensive dataset with carbon emission factors. data = {     "activity": ["driving", "flying", "electricity", "meat_diet", "public_transport"],     "carbon_footprint": [0.4, 0.2, 0.3, 0.5, 0.1]  # Example emission factors (tons CO2/year)} df = pd.DataFrame(data)# Train a simple ML model (for demonstration) X = pd.get_dummies(df["activity"])  # Convert categorical data to numerical y = df["carbon_footprint"] X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) model = RandomForestRegressor() model.fit(X_train, y_train)# Home route@app.route("/", methods=["GET", "POST"])def home():     if request.method == "POST":         # Get user inputs         activity = request.form["activity"]         hours = float(request.form["hours"])          # Predict carbon footprint         activity_encoded = pd.get_dummies(pd.Series([activity]))         activity_encoded = activity_encoded.reindex(columns=X.columns, fill_value=0)         predicted_footprint = model.predict(activity_encoded)[0] * hours          return render_template("result.html", activity=activity, footprint=predicted_footprint)     return render_template("index.html")# Run the appif __name__ == "__main__":     app.run(debug=True)3. HTML Templates

Create a folder named templates in the same directory as your Python script. Inside it, create two files: index.html and result.html.

index.html

<!DOCTYPE html><html lang="en"><head>     <meta charset="UTF-8">     <meta name="viewport" content="width=device-width, initial-scale=1.0">     <title>EcoTrack - Carbon Footprint Calculator</title></head><body>     <h1>EcoTrack</h1>     <p>Calculate your carbon footprint!</p>     <form method="POST">         <label for="activity">Select Activity:</label>         <select name="activity" id="activity">             <option value="driving">Driving</option>             <option value="flying">Flying</option>             <option value="electricity">Electricity Usage</option>             <option value="meat_diet">Meat Diet</option>             <option value="public_transport">Public Transport</option>         </select>         <br><br>         <label for="hours">Hours/Days per Year:</label>         <input type="number" name="hours" id="hours" required>         <br><br>         <button type="submit">Calculate</button>     </form></body></html>

result.html

<!DOCTYPE html><html lang="en"><head>     <meta charset="UTF-8">     <meta name="viewport" content="width=device-width, initial-scale=1.0">     <title>EcoTrack - Result</title></head><body>     <h1>EcoTrack</h1>     <p>Your carbon footprint for <strong>{{ activity }}</strong> is:</p>     <h2>{{ footprint }} tons CO2/year</h2> </body></html>


4. Run the Application

  1.	Save the Python script as app.py.
  2.	Create the templates folder and add the HTML files.
  3.	Run the Flask app:
  4.	bash
  5.	Copy
  6.	python app.py
  7.	Open your browser and go to http://127.0.0.1:5000/ to use the app.

Import librariesfrom flask 
import Flask, request, render_template 
import pandas as pd 
import numpy as np from sklearn.ensemble 
import RandomForestRegressor from sklearn.model_selection 
import train_test_split # Initialize Flask app app = Flask(name)

# Load a sample dataset (for demonstration)
# In a real-world scenario, use a comprehensive dataset with carbon emission factors. 
data = { "activity": ["driving", "flying", "electricity", "meat_diet", "public_transport"], "carbon_footprint": [0.4, 0.2, 0.3, 0.5, 0.1] # Example emission factors (tons CO2/year)} 
df = pd.DataFrame(data)

# Train a simple ML model (for demonstration) 
X = pd.get_dummies(df["activity"]) 

# Convert categorical data to numerical 
y = df["carbon_footprint"] X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor() model.fit(X_train, y_train)
# Home route@app.route("/", methods=["GET", "POST"])def home(): if request.method == "POST": 

# Get user inputs activity = request.form["activity"] hours = float(request.form["hours"]) 
# Predict carbon footprint 
activity_encoded = pd.get_dummies(pd.Series([activity])) 
activity_encoded = activity_encoded.reindex(columns=X.columns, fill_value=0) 
predicted_footprint = model.predict(activity_encoded)[0] * hours 

return render_template("result.html", activity=activity, footprint=predicted_footprint) 
return render_template("index.html")
# Run the appif 
name == "main": app.run(debug=True)3. 
HTML Templates
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset_
data = pd.read_csv("ipl.csv",usecols=["team1","team2","venue","city","toss_winner","winner"])

# Keep only required columns
data = data[['team1', 'team2', 'venue', 'city', 'toss_winner', 'winner']]

# Remove missing values
data = data.dropna()

# Features (Input)
X = data[['team1', 'team2', 'venue', 'city', 'toss_winner']]

# Target (Output)
y = data['winner']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text columns into numbers
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'),
         ['team1', 'team2', 'venue', 'city', 'toss_winner'])
    ]
)

# Create the model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(random_state=42))
])

# Train the model
model.fit(X_train, y_train)

# Save the trained model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")
print("model.pkl has been created.")
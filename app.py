from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    team1 = request.form['team1']
    team2 = request.form['team2']
    venue = request.form['venue']
    city = request.form['city']
    toss_winner = request.form['toss_winner']

    data = pd.DataFrame({
        'team1': [team1],
        'team2': [team2],
        'venue': [venue],
        'city': [city],
        'toss_winner': [toss_winner]
    })

    prediction = model.predict(data)

    return render_template(
        "index.html",
        prediction_text="Predicted Winner: " + prediction[0]
    )

if __name__ == "__main__":
    app.run(debug=True)
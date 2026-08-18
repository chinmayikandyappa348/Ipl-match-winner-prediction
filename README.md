🏏 IPL Match Winner Prediction Using Machine Learning

📌 Project Overview

This is a minor Data Science and Machine Learning project that predicts the likely winner of an IPL cricket match using historical match information.

The project uses Python, Scikit-learn, and Flask to develop a simple Machine Learning-based prediction application.

🎯 Objectives

- Analyze IPL match data
- Preprocess the data
- Select relevant features
- Train a Machine Learning classification model
- Predict the likely match winner
- Develop a simple Flask web application
 
🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Flask
- HTML
- CSS

🤖 Machine Learning Algorithm

Random Forest Classifier

The model is trained using selected match-related features such as teams, venue, city, and toss winner.

📂 Project Structure

ipl-match-winner-prediction/
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── main.py
├── predict.py
├── train_model.py
├── requirements.txt
└── README.md

📊 Dataset

The IPL historical dataset is required for training the model.

Due to the large size of the dataset, "ipl.csv" is not included in this GitHub repository.

The dataset should be placed in the project folder as:

ipl.csv

🤖 Trained Model

The trained "model.pkl" file is also not included in this repository because of its large file size.

After obtaining the dataset, generate the model by running:

python train_model.py

This will create the required trained model file.

🚀 How to Run

Step 1: Install the required libraries

pip install -r requirements.txt

Step 2: Place the dataset

Place the required IPL dataset in the project folder:

ipl.csv

Step 3: Train the model

python train_model.py

This generates the trained model file.

Step 4: Run the Flask application

python main.py

Step 5: Open the application

Open the local address shown in the terminal, usually:

http://127.0.0.1:5000/

🔄 Project Workflow

IPL Historical Dataset
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Categorical Encoding
        ↓
Model Training
        ↓
Random Forest Classifier
        ↓
Match Winner Prediction
        ↓
Flask Web Application

📚 Learning Outcomes

This project helped me gain practical experience in:

- Python programming
- Data preprocessing
- Machine Learning classification
- Random Forest
- Feature selection
- Model training
- Flask web development
- Building an end-to-end Machine Learning project

🚀 Future Improvements

- Include player performance statistics
- Add recent team performance
- Include batting and bowling statistics
- Add head-to-head team records
- Experiment with additional Machine Learning algorithms
- Improve the web interface
- Deploy the application online

👩‍💻 Author

Chinmayi k

BCA Student | Data Science Learner

---

⭐ Minor Data Science & Machine Learning Project

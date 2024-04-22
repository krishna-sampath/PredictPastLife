from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained models
clf_trait = joblib.load('personality_trait_model.pkl')
clf_descriptor = joblib.load('personality_descriptor_model.pkl')

# Prediction function for both trait and descriptor
def predict_personality(year, month, day):
    trait_prediction = clf_trait.predict([[year, month, day]])
    descriptor_prediction = clf_descriptor.predict([[year, month, day]])
    return f"The person born on the date {day}-{month}-{year} was a {trait_prediction[0]} {descriptor_prediction[0]} in their past life."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    year = int(request.form['year'])
    month = int(request.form['month'])
    day = int(request.form['day'])
    text = predict_personality(year, month, day)
    return render_template('result.html', text = text)

if __name__ == '__main__':
    app.run(debug=True)

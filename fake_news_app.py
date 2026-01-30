from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


model = joblib.load(os.path.join(BASE_DIR, "fake_news_pred_model_1.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    news=""
    news = request.form['news']
    news_vector = vectorizer.transform([news])
    prediction = model.predict(news_vector)

    result = "REAL NEWS 📰" if prediction[0] == 1 else "FAKE NEWS ❌"
    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)





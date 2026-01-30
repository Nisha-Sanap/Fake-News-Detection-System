
---

# 📰 TruthLens – Fake News Detector

**TruthLens** is a web-based **Fake News Detection System** that uses **Machine Learning** to classify news as **Real** or **Fake**. The system combines **Natural Language Processing (NLP)** with a clean **Flask web interface**, allowing users to quickly verify the authenticity of news headlines.

This project is perfect for **students, developers, and educators** who want to explore AI-powered text classification or build real-world ML applications.

---

## 🚀 Features

- Classifies news as **Fake** or **Real** using ML.
- Uses **TF-IDF Vectorizer** for text feature extraction.
- **Pre-trained classification model** for fast predictions.
- User-friendly **Flask web application**.
- Responsive and visually appealing **HTML/CSS interface**.
- Upload or enter news text for instant analysis.
- Displays confidence level and explanation for predictions.

---

## 🛠️ Technologies Used

### Programming Language
- Python 3

### Machine Learning
- Scikit-learn
- NLP (TF-IDF Vectorizer)
- Pre-trained classification model
-numpy
-pandas

### Web Development
- Flask
- HTML
- CSS 3
- Bootstrap 5
- Font Awesome Icons

---

## 📂 Project Structure

```text
TruthLens/
│
├── fake_news_project.ipynb        # Jupyter notebook for model training and testing
├── fake_news_app.py               # Flask web application
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
├── .gitignore                     # Ignored files/folders in Git
│
├── templates/
│   └── index.html                 # Frontend HTML page
│
├── screenshots/
│   ├── home.png                   # Home page screenshot
│   └── result.png                 # Prediction result page screenshot
│
├── fake_news_pred_model_1.pkl     # Pre-trained ML model
└── vectorizer.pkl                 # TF-IDF vectorizer


---
```

 ## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

 ```bash
 git clone https://github.com/your-username/TruthLens.git
 cd TruthLens
```
---

### 2️⃣ Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / Mac**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```



## ▶️ Running the Application

Start the Flask app:

```bash
python fake_news_app.py
```

Open a web browser and navigate to:

```
http://127.0.0.1:5000/
```

You can now **enter news text** or **upload headlines** to check if the news is **Fake or Real**.

---

## 📸 Screenshots

### 🔹 Home Page

![Home Page](screenshots/home.png)

### 🔹 Prediction Result

![Result Page](screenshots/result.png)

---

## 📊 Dataset

The ML model is trained on a labeled **fake news dataset**.

* Features extracted using **TF-IDF Vectorizer**.
* Trained model uses **scikit-learn classifiers** (like Logistic Regression, Naive Bayes, or SVM).

> Dataset is included as `news_dataset.csv.zip` for academic and educational purposes.

---

## 🎯 Use Cases

* Detect fake news articles online.
* Verify news headlines for competitive exams.
* Educational projects on **Machine Learning and NLP**.
* Research projects on **text classification**.
* AI-powered content verification for social media platforms.

---

## 👩‍💻 Author

**Nisha Sanap**
Computer Engineering Student

* GitHub: [https://github.com/Nisha-Sanap](https://github.com/Nisha-Sanap)

---

## 📜 License

This project is intended for **educational purposes only**.
Feel free to use it for learning, development, or academic projects.

---

## 💡 Notes

* Make sure **`fake_news_pred_model_1.pkl`** and **`vectorizer.pkl`** are in the main project folder.
* Ensure **Python 3** and **required packages** are installed.
* The application is optimized for **text-based news headlines** only.

````

---


